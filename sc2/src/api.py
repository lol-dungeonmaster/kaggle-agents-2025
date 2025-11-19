import json, logging, platform, requests, threading, time
from enum import Enum
from google import genai
from google.api_core import retry, exceptions
from google.genai import errors
from threading import Timer
from typing import Callable, NewType, NamedTuple
from .secret import UserSecretsClient

is_retriable = lambda e: (isinstance(e, errors.APIError) and e.code in {429, 503, 500})

class GeminiModel:
    def __init__(self, rpm: list, tpm: list, rpd: list):
        self.rpm = rpm # requests per minute
        self.tpm = tpm # tokens per minute in millions
        self.rpd = rpd # requests per day
        self.err = [0,0] # validation, api_related

# A python api-helper with model fail-over/chaining/retry support.
GeminiEmbedFunction = NewType("GeminiEmbedFunction", None) # forward-decl
class Api:
    gen_limit_in = 1048576
    emb_limit_in = 2048
    gen_model = {
        "gemini-2.0-flash": GeminiModel([15,2000,10000,30000],[1,4,10,30],[200,inf,inf,inf]), # stable wo/thinking: 15 RPM/1M TPM/200 RPD
        "gemini-2.0-flash-exp": GeminiModel([15,2000,10000,30000],[1,4,10,30],[200,inf,inf,inf]), # latest w/thinking: 15 RPM/1M TPM/200 RPD
        "gemini-2.5-flash-preview-09-2025": GeminiModel([10,1000,2000,10000],[.25,1,3,8],[250,10000,100000,inf]), # exp: 10 RPM/250K TPM/250 RPD
        "gemini-2.5-flash": GeminiModel([10,1000,2000,10000],[.25,1,3,8],[250,10000,100000,inf]), # stable: 10 RPM/250K TPM/250 RPD
        "gemini-2.5-flash-lite-preview-09-2025": GeminiModel([15,4000,10000,30000],[.25,4,10,30],[1000,inf,inf,inf]), # exp: 15 RPM/250K TPM/1K RPD
        "gemini-2.5-flash-lite": GeminiModel([15,4000,10000,30000],[.25,4,10,30],[1000,inf,inf,inf]), # stable: 15 RPM/250K TPM/1K RPD
        "gemini-2.5-pro": GeminiModel([5,150,1000,2000],[.25,2,5,8],[100,10000,50000,inf]), # stable: 5 RPM/250K TPM/100 RPD
    }
    gen_local = ["gemma3n:e4b","gemma3:12b-it-qat"]
    default_local = 0
    default_model = []
    embed_model = "gemini-embedding-001", GeminiModel([100,3000,5000,10000],[.03,1,5,10],[1000,inf,inf,inf]) # stable: 100 RPM/30K TPM/1000 RPD/100 per batch
    embed_local = False
    error_total = 0
    min_rpm = 3
    dt_between = 2.0
    errored = False
    running = False
    dt_err = 60.0
    dt_rpm = 60.0

    @classmethod
    def get(cls, url: str):
        # Create a header matching the OS' tcp-stack fingerprint.
        system_ua = None
        match platform.system():
            case 'Linux':
                system_ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
            case 'Darwin':
                system_ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 15_7_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Safari/605.1.15'
            case 'Windows':
                system_ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'
        try:
            request = requests.get(url, headers={'User-Agent': system_ua})
            if request.status_code != requests.codes.ok:
                print(f"Gemini.get() returned status {request.status_code}")
            return request.text
        except Exception as e:
            raise e

    class Limit(Enum):
        FREE = 0
        TIER_1 = 1
        TIER_2 = 2
        TIER_3 = 3
    
    class Model(Enum):
        GEN = 1
        EMB = 2
        LOC = 3

    class Const(Enum):
        STOP = "I don't know."
        METRIC_BATCH = 20
        SERIES_BATCH = 40
        EMBED_BATCH = 100
        CHUNK_MAX = 1500

        @classmethod
        def Stop(cls):
            return cls.STOP.value

        @classmethod
        def MetricBatch(cls):
            return cls.METRIC_BATCH.value

        @classmethod
        def SeriesBatch(cls):
            return cls.SERIES_BATCH.value

        @classmethod
        def EmbedBatch(cls):
            return cls.EMBED_BATCH.value

        @classmethod
        def ChunkMax(cls):
            return cls.CHUNK_MAX.value
    
    class Env(NamedTuple): # Make init args immutable.
        CLIENT: genai.Client
        API_LIMIT: int
        GEN_DEFAULT: str

    def __init__(self, with_limit: Limit, default_model: str):
        if default_model in self.gen_model.keys():
            self.write_lock = threading.RLock()
            self.args = Api.Env(
                genai.Client(api_key=UserSecretsClient().get_secret("GOOGLE_API_KEY")),
                with_limit.value,
                default_model)
            self.m_id = list(self.gen_model.keys()).index(default_model)
            self.default_model.append(default_model)
            self.gen_rpm = list(self.gen_model.values())[self.m_id].rpm[self.args.API_LIMIT]
            self.s_embed = GeminiEmbedFunction(self.args.CLIENT, semantic_mode = True) # type: ignore
            logging.getLogger("google_genai").setLevel(logging.WARNING) # suppress info on generate
        else:
            print(f"{default_model} not found in gen_model.keys()")
        

    def __call__(self, model: Model) -> str:
        if model == self.Model.GEN:
            return "models/" + list(self.gen_model.keys())[self.m_id]
        elif model == self.Model.LOC:
            return self.gen_local[self.default_local]
        else:
            return "models/" + self.embed_model[0] if not self.embed_local else "embeddinggemma:latest"

    def push_default_model(self, model_id: str):
        if model_id in self.gen_model.keys():
            self.write_lock.acquire()
            self.stop_running()
            self.default_model.append(model_id)
            self.m_id = list(self.gen_model.keys()).index(model_id)
            self.write_lock.release()
        else:
            print(f"{model_id} not found in gen_model.keys()")

    def pop_default_model(self):
        if len(self.default_model) > 1:
            self.write_lock.acquire()
            self.stop_running()
            self.default_model.pop(-1)
            self.m_id = list(self.gen_model.keys()).index(self.default_model[-1])
            self.write_lock.release()

    def retriable(self, retry_fn: Callable, *args, **kwargs):
        for attempt in range(len(self.gen_model.keys())):
            try:
                self.write_lock.acquire()
                if self.gen_rpm > self.min_rpm:
                    self.gen_rpm -= 1
                else:
                    self.on_error(kwargs)
                if not self.running and not self.errored:
                    self.rpm_timer = Timer(self.dt_rpm, self.refill_rpm)
                    self.rpm_timer.start()
                    self.running = True
                return retry_fn(*args, **kwargs)
            except (errors.APIError, exceptions.RetryError) as api_error:
                if isinstance(api_error, errors.APIError):
                    is_retry = api_error.code in {429, 503, 500, 400} # code 400 when TPM exceeded
                    if not is_retry or attempt == len(self.gen_model.keys())-1:
                        raise api_error
                self.on_error(kwargs)
            except Exception as e:
                raise e
            finally:
                self.write_lock.release()

    def on_error(self, kwargs):
        self.generation_fail()
        kwargs["model"] = self(Api.Model.GEN)
        time.sleep(self.dt_between)

    def stop_running(self):
        if self.running:
            self.rpm_timer.cancel()
            self.running = False

    def validation_fail(self):
        list(self.gen_model.values())[self.m_id].err[0] += 1
        self.error_total += 1

    def generation_fail(self):
        self.stop_running()
        self.save_error()
        self.next_model()
        print("api.generation_fail.next_model: model is now ", list(self.gen_model.keys())[self.m_id])
        if not self.errored:
            self.error_timer = Timer(self.dt_err, self.zero_error)
            self.error_timer.start()
            self.errored = True

    def save_error(self):
        list(self.gen_model.values())[self.m_id].err[1] += 1
        self.error_total += 1

    def next_model(self):
        self.m_id = (self.m_id+1)%len(self.gen_model.keys())
        self.gen_rpm = list(self.gen_model.values())[self.m_id].rpm[self.args.API_LIMIT]

    def refill_rpm(self):
        self.running = False
        self.gen_rpm = list(self.gen_model.values())[self.m_id].rpm[self.args.API_LIMIT]
        print("api.refill_rpm ", self.gen_rpm)

    def zero_error(self):
        self.errored = False
        self.m_id = list(self.gen_model.keys()).index(self.default_model[-1])
        self.gen_rpm = list(self.gen_model.values())[self.m_id].rpm[self.args.API_LIMIT]
        print("api.zero_error: model is now ", list(self.gen_model.keys())[self.m_id])

    def token_count(self, expr: str):
        count = self.args.CLIENT.models.count_tokens(
            model=self(Api.Model.GEN),
            contents=json.dumps(expr))
        return count.total_tokens

    def errors(self):
        errors = {"total": self.error_total, "by_model": {}}
        for m_code, m in self.gen_model.items():
            errors["by_model"].update({
                m_code: {
                    "api_related": m.err[1],
                    "validation": m.err[0]
                }})
        return errors

    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def similarity(self, content: list):
        return self.s_embed.sts(content) # type: ignore