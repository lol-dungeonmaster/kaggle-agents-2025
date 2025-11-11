# Environment Setup


```python
# Setup the notebook based on running environment.
import os
# Optional: Enable telemetry in browser_use and chromadb.
os.environ["ANONYMIZED_TELEMETRY"] = "false"
# Check for kaggle environment.
if os.getenv("KAGGLE_KERNEL_RUN_TYPE"):
    # Kaggle Run: update the system.
    !pip uninstall -qqy google-ai-generativelanguage pydrive2 tensorflow cryptography pyOpenSSL langchain langchain-core nltk ray click google-generativeai google-cloud-translate datasets cesium bigframes plotnine mlxtend fastai spacy thinc google-colab gcsfs jupyter-kernel-gateway
    !pip install -qU posthog\<6.0.0 google-genai==1.45.0 chromadb==0.6.3 opentelemetry-proto==1.37.0
    !pip install -qU langchain-community langchain-text-splitters wikipedia lmnr[all] google-adk
    from kaggle_secrets import UserSecretsClient # type: ignore
    from jupyter_server.serverapp import list_running_servers # type: ignore
else:
    # Mock the kaggle secrets client.
    class UserSecretsClient:
        @classmethod
        def set_secret(cls, id: str, value: str):
            os.environ[id] = value
        @classmethod
        def get_secret(cls, id: str):
            try:
                return os.environ[id]
            except KeyError as e:
                print(f"KeyError: authentication token for {id} is undefined")
    # Local Run: update the venv.
    %pip install -qU posthog\<6.0.0 google-genai==1.45.0 chromadb==0.6.3 opentelemetry-proto==1.37.0
    %pip install -qU langchain-community langchain-text-splitters wikipedia pandas google-api-core "lmnr[all]" browser-use ollama google-adk
    from browser_use import Agent as BrowserAgent

import ast, chromadb, json, logging, pandas, platform, pytz, re, requests, time, warnings, wikipedia
from bs4 import Tag
from chromadb import Documents, Embeddings
from datetime import datetime, timedelta
from dateutil.parser import parse
from enum import Enum
from google import genai
from google.api_core import retry, exceptions
from google.genai.models import Models
from google.genai import types, errors
from IPython.display import Markdown, display, HTML
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters.html import HTMLSemanticPreservingSplitter
from langchain_text_splitters.json import RecursiveJsonSplitter
from lmnr import Laminar
from math import inf
from pydantic import BaseModel, field_validator
from threading import Timer
from tqdm import tqdm
from typing import Optional, Callable, NewType
from wikipedia.exceptions import DisambiguationError, PageError
```

    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m45.8/45.8 kB[0m [31m2.2 MB/s[0m eta [36m0:00:00[0m
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m67.3/67.3 kB[0m [31m3.8 MB/s[0m eta [36m0:00:00[0m
    [?25h  Installing build dependencies ... [?25l[?25hdone
      Getting requirements to build wheel ... [?25l[?25hdone
      Preparing metadata (pyproject.toml) ... [?25l[?25hdone
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m238.5/238.5 kB[0m [31m10.6 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m611.1/611.1 kB[0m [31m23.5 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m2.4/2.4 MB[0m [31m65.1 MB/s[0m eta [36m0:00:00[0m:00:01[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m105.4/105.4 kB[0m [31m6.0 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m278.2/278.2 kB[0m [31m16.7 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m2.0/2.0 MB[0m [31m62.3 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m103.1/103.1 kB[0m [31m5.9 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m17.4/17.4 MB[0m [31m82.0 MB/s[0m eta [36m0:00:00[0m:00:01[0m00:01[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m107.3/107.3 kB[0m [31m6.4 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m456.6/456.6 kB[0m [31m24.9 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m128.4/128.4 kB[0m [31m6.6 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m3.8/3.8 MB[0m [31m81.9 MB/s[0m eta [36m0:00:00[0m:00:01[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m456.1/456.1 kB[0m [31m23.0 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m46.0/46.0 kB[0m [31m2.8 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m86.8/86.8 kB[0m [31m4.4 MB/s[0m eta [36m0:00:00[0m
    [?25h  Building wheel for pypika (pyproject.toml) ... [?25l[?25hdone
      Preparing metadata (setup.py) ... [?25l[?25hdone
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m2.5/2.5 MB[0m [31m48.5 MB/s[0m eta [36m0:00:00[0m:00:01[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m1.0/1.0 MB[0m [31m38.9 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m471.2/471.2 kB[0m [31m23.2 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m253.7/253.7 kB[0m [31m12.7 MB/s[0m eta [36m0:00:00[0m
    [2K   [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m357.5/357.5 kB[0m [31m17.1 MB/s[0m eta [36m0:00:00[0m
    [?25h  Building wheel for wikipedia (setup.py) ... [?25l[?25hdone



```python
# Prepare the Gemini api for use.
# Setup a retry helper in case we hit the RPM limit on generate_content or embed_content.
is_retriable = lambda e: (isinstance(e, errors.APIError) and e.code in {429, 503, 500})
Models.generate_content = retry.Retry(predicate=is_retriable)(Models.generate_content)
Models.embed_content = retry.Retry(predicate=is_retriable)(Models.embed_content)

# Activate Laminar auto-instrumentation.
try:
    Laminar.initialize(project_api_key=UserSecretsClient().get_secret("LMNR_PROJECT_API_KEY"))
except:
    print("Skipping Laminar.initialize()")

class GeminiModel:
    def __init__(self, rpm: list, tpm: list, rpd: list):
        self.rpm = rpm # requests per minute
        self.tpm = tpm # tokens per minute in millions
        self.rpd = rpd # requests per day
        self.err = [0,0] # validation, api_related

# A python api-helper with model fail-over/chaining/retry support.
GeminiEmbedFunction = NewType("GeminiEmbedFunction", None) # forward-decl
class Gemini:
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
    dt_err = 45.0
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
                print(f"api.get() returned status {request.status_code}")
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

    def __init__(self, with_limit: Limit, default_model: str):
        self.client = genai.Client(api_key=UserSecretsClient().get_secret("GOOGLE_API_KEY"))
        self.limit = with_limit.value
        self.m_id = list(self.gen_model.keys()).index(default_model)
        self.push_default_model(default_model)
        self.gen_rpm = list(self.gen_model.values())[self.m_id].rpm[self.limit]
        self.s_embed = GeminiEmbedFunction(self.client, semantic_mode = True) # type: ignore
        logging.getLogger("google_genai").setLevel(logging.WARNING) # suppress info on generate

    def __call__(self, model: Model) -> str:
        if model == self.Model.GEN:
            return "models/" + list(self.gen_model.keys())[self.m_id]
        elif model == self.Model.LOC:
            return self.gen_local[self.default_local]
        else:
            return "models/" + self.embed_model[0] if not self.embed_local else "embeddinggemma:latest"

    def push_default_model(self, model_code: str):
        if model_code in self.gen_model.keys():
            self.stop_running()
            self.default_model.append(model_code)
            self.m_id = list(self.gen_model.keys()).index(model_code)
        else:
            print(f"{model_code} not found in gen_model.keys()")

    def pop_default_model(self):
        self.stop_running()
        self.default_model.pop(-1)
        self.m_id = list(self.gen_model.keys()).index(self.default_model[-1])

    def retriable(self, retry_fn: Callable, *args, **kwargs):
        for attempt in range(len(self.gen_model.keys())):
            try:
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
                    retriable = api_error.code in {429, 503, 500, 400} # code 400 when TPM exceeded
                    if not retriable or attempt == len(self.gen_model.keys())-1:
                        raise api_error
                self.on_error(kwargs)
            except Exception as e:
                raise e

    def on_error(self, kwargs):
        self.generation_fail()
        kwargs["model"] = self(Gemini.Model.GEN)
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
        self.gen_rpm = list(self.gen_model.values())[self.m_id].rpm[self.limit]

    def refill_rpm(self):
        self.running = False
        self.gen_rpm = list(self.gen_model.values())[self.m_id].rpm[self.limit]
        print("api.refill_rpm ", self.gen_rpm)

    def zero_error(self):
        self.errored = False
        self.m_id = list(self.gen_model.keys()).index(self.default_model[-1])
        self.gen_rpm = list(self.gen_model.values())[self.m_id].rpm[self.limit]
        print("api.zero_error: model is now ", list(self.gen_model.keys())[self.m_id])

    def token_count(self, expr: str):
        count = self.client.models.count_tokens(
            model=self(Gemini.Model.GEN),
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
```

    Skipping Laminar.initialize()



```python
# Define the embedding function.
api = NewType("Gemini", None) # type: ignore (forward-decl)
class GeminiEmbedFunction:
    document_mode = True  # Generate embeddings for documents (T,F), or queries (F,F).
    semantic_mode = False # Semantic text similarity mode is exclusive (F,T).
    
    def __init__(self, genai_client, semantic_mode: bool = False):
        self.client = genai_client
        if semantic_mode:
            self.document_mode = False
            self.semantic_mode = True

    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def __embed__(self, input: Documents) -> Embeddings:
        if self.document_mode:
            embedding_task = "retrieval_document"
        elif not self.document_mode and not self.semantic_mode:
            embedding_task = "retrieval_query"
        elif not self.document_mode and self.semantic_mode:
            embedding_task = "semantic_similarity"
        partial = self.client.models.embed_content(
            model=api(Gemini.Model.EMB),
            contents=input,
            config=types.EmbedContentConfig(task_type=embedding_task)) # type: ignore
        return [e.values for e in partial.embeddings]
    
    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def __call__(self, input: Documents) -> Embeddings:
        try:
            response = []
            for i in range(0, len(input), Gemini.Const.EmbedBatch()):  # Gemini max-batch-size is 100.
                response += self.__embed__(input[i:i + Gemini.Const.EmbedBatch()])
            return response
        except Exception as e:
            print(f"caught exception of type {type(e)}\n{e}")
            raise e

    def sts(self, content: list) -> float:
        df = pandas.DataFrame(self(content), index=content)
        score = df @ df.T
        return score.iloc[0].iloc[1]
```

## Set Gemini API Limit


```python
# Instantiate the api-helper with usage limit => FREE.
api = Gemini(with_limit=Gemini.Limit.FREE, default_model="gemini-2.0-flash") # [FREE,TIER_1,TIER_2,TIER_3]
```

# Gemini Baseline Check


```python
# This is an accurate retelling of events. 
config_with_search = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())],
    temperature=0.0
)

chat = api.client.chats.create(
    model=api(Gemini.Model.GEN), 
    config=config_with_search, 
    history=[]) # Ignoring the part about dark elves, and tengwar.

response = chat.send_message('Do you know anything about the stock market?')
Markdown(response.text)
```




Yes, I do. The stock market is a place where shares of publicly traded companies are bought and sold. It allows companies to raise capital and investors to potentially grow their wealth. The stock market can influence the products you buy, the jobs available, and even your retirement plans.

Here are some key aspects of the stock market:

*   **Function:** Companies issue shares on the stock market to raise capital for business expansion. Investors buy shares to potentially receive dividends, vote in corporate elections, or sell the shares at a higher price.
*   **Participants:** The stock market involves both investors and traders. Investors typically take a long-term approach, while traders aim to capitalize on short-term market volatility.
*   **Exchanges:** Stocks are bought and sold on exchanges, such as the New York Stock Exchange (NYSE) and the Nasdaq. These exchanges provide a platform for trading and act as guarantors of settlement.
*   **Market Size:** The stock market has grown significantly over the years. The total market capitalization of all publicly traded stocks worldwide rose from US$2.5 trillion in 1980 to US$111 trillion by the end of 2023.
*   **Market Indicators:** The stock market is often considered an indicator of a country's economic strength and development. Rising share prices tend to be associated with increased business investment.






```python
response = chat.send_message('I have an interest in AMZN stock')
Markdown(response.text)
```




Okay, I can provide you with some information regarding AMZN (Amazon) stock. Based on the most recent information available, here's a summary:

**Current Status:**

*   As of November 8, 2025, AMZN is trading around $244.41 - $245.10.
*   Amazon's market capitalization is approximately $2.61 trillion.
*   The stock has fluctuated between $238.49 and $245.50 today.
*   The 52-week range is $161.38 to $258.60.
*   The next earnings report is expected on January 29, 2026.

**Analyst Ratings and Price Targets:**

*   The consensus among analysts is "Strong Buy".
*   The average price target from analysts is around $296.26 - $297.03.
*   Some analysts have a high forecast of $340.

**Forecasts for the End of 2025:**

*   Predictions vary, but several sources suggest a price between $214 and $298 by the end of 2025.
*   One source estimates AMZN will hit $250 by the end of 2025.
*   Another projects a range of $242.89 and $296.87, with an average near $269.88.

**Factors Influencing the Stock Price:**

*   **Earnings Reports:** Amazon's share price is impacted by quarterly earnings. The last earnings report beat expectations.
*   **AWS Growth:** Amazon Web Services (AWS), particularly its AI-fueled growth, is a key driver.
*   **Consumer Spending:** Consumer spending trends influence Amazon's revenue and profitability, especially in retail.
*   **Economic Conditions:** High inflation, changes in consumer spending, and interest rate hikes can all have an impact.
*   **New Initiatives:** New business initiatives can also affect the stock price.
*   **Cloud Computing Demand:** Changes in cloud computing demand influence the stock price.

**Recent News and Developments:**

*   Amazon signed a multiyear deal with OpenAI for computing power.
*   Amazon is launching a low-cost shopping app, Amazon Bazaar, in multiple countries.
*   New Echo products with upgraded Alexa and AZ3 chips are being launched.

**General Sentiment:**

*   The overall sentiment is bullish, with analysts optimistic about Amazon's short-term prospects.
*   Amazon is considered a leader in e-commerce with opportunities for growth.

**Important Note:** Stock market investments can be risky, and forecasts are not guaranteed. You should consult with a financial advisor before making any investment decisions.





```python
response = chat.send_message('''Tell me about AMZN current share price, short-term trends, and bullish versus bearish predictions''')
Markdown(response.text)
```




Here's an overview of AMZN (Amazon) stock, including its current share price, short-term trends, and bullish versus bearish predictions:

**Current Share Price:**

*   As of November 8, 2025, the current price of AMZN is around $244.41.
*   Throughout the day, AMZN has fluctuated between $238.49 and $245.50.

**Short-Term Trends:**

*   **Mixed Signals:** AMZN has shown a 0.56% increase in the last 24 hours. However, it has fallen by -2.28% compared to the previous week.
*   **Positive Recent Performance:** The price has risen in 7 of the last 10 days and is up by 9.01% over the past 2 weeks.
*   **Technical Indicators:** Technical analysis indicates a bullish sentiment in the short term.
*   **Horizontal Trend:** The stock is moving within a wide and horizontal trend, which is expected to continue.
*   **Support and Resistance:** The $240-$245 range is considered a strong support level.

**Bullish Predictions:**

*   **Strong Buy Consensus:** The consensus rating among analysts is "Strong Buy".
*   **Upside Potential:** The average price target from analysts is around $296.26, suggesting an upside potential of over 18%. Some analysts have a high forecast of $340.
*   **Revenue Growth:** Amazon's revenue is expected to rise significantly in the coming years.
*   **AWS and AI:** Growth in Amazon Web Services (AWS), fueled by AI, is a key driver for bullish sentiment.
*   **Analyst Upgrades:** Analysts are raising price targets, citing Amazon's role in the AI ecosystem.
*   **Long-Term Growth:** Bullish forecasts see the share price potentially reaching $431 by 2030.

**Bearish Predictions:**

*   **Potential Downturn:** Some forecasts predict a slight decrease in the short term, with one source suggesting a price of $242.71 by December 7, 2025.
*   **Overbought Conditions:** Amazon's Relative Strength Index (RSI) is above 70, signaling overbought conditions, which could lead to a pullback.
*   **Profit-Taking:** After a sharp move higher, some profit-taking could occur, especially if the broader market declines.
*   **Long-Term Bearish Case:** A bearish scenario suggests the stock price could range between $233.09 and $350.88 in 2030.
*   **Sell Signal:** One source indicates a massive sell signal on the 1-week time frame as the price hit a 5-year Higher Highs trendline.

**In summary:** The prevailing sentiment leans towards a bullish outlook for AMZN, driven by strong fundamentals, growth in AWS and AI, and positive analyst ratings. However, some technical indicators suggest the possibility of a short-term pullback.





```python
response = chat.send_message('''What is mgm studio's stock ticker symbol?''')
Markdown(response.text)
```




Please note that there seems to be some confusion. MGM Studios was acquired by Amazon in 2022 and is no longer a publicly traded company with its own stock ticker.

The ticker symbol "MGM" refers to MGM Resorts International, a hospitality and entertainment company. It trades on the New York Stock Exchange (NYSE) under the ticker symbol "MGM". As of November 7, 2025, the stock price for MGM Resorts International was $32.66.





```python
response = chat.send_message('''What was the last open,close,high,low data for AMZN again?''')
Markdown(response.text)
```




Here's the requested data for AMZN (Amazon) as of November 7, 2025:

*   **Open:** $242.90 or $242.99
*   **Close:** $244.41
*   **High:** $244.90 or $245.50
*   **Low:** $238.49





```python
response = chat.send_message('''What is AMZN open,close,high,low data for the past month? 
Present the data with multiple columns for display in markdown.''')
Markdown(response.text)
```




It is difficult to provide exact, real-time intraday historical data for the past month (October 9, 2025 - November 8, 2025) without access to a specialized financial data service. However, I can provide a sample of the data available from the beginning of November 2025, and some data points from late October 2025 to give you an idea.

**Please note:** This is not a complete dataset, and real-time data may vary.

| Date       | Open      | Close     | High      | Low       |
| :----------- | :-------- | :-------- | :-------- | :-------- |
| Nov 7, 2025  | $242.90   | $244.41   | $244.90   | $238.49   |
| Nov 6, 2025  | $249.16   | $243.04   | $250.38   | $242.17   |
| Nov 5, 2025  | $249.03   | $250.20   | $251.00   | $246.16   |
| Nov 4, 2025  | $250.38   | $249.32   | $257.01   | $248.66   |
| Nov 3, 2025  | $255.36   | $254.00   | $258.60   | $252.90   |
| Oct 31, 2025 | $250.10   | $244.22   | $250.50   | $243.98   |
| Oct 30, 2025 | $227.06   | $222.86   | $228.44   | $222.75   |
| Oct 29, 2025 | $231.67   | $230.30   | $232.82   | $227.76   |
| Oct 28, 2025 | $228.22   | $229.25   | $231.49   | $226.21   |
| Oct 27, 2025 | $227.66   | $226.97   | $228.40   | $225.54   |
| Oct 26, 2025 | $221.09   | $224.21   | N/A       | N/A       |

For more precise data, I recommend consulting a financial data provider like Nasdaq, or Trading Economics.




# Previously on Kaggle: StockChat 1.0

## Validation BaseModels


```python
# Validation BaseModels in pydantic schema.
class RestStatus(Enum):
    OK = "OK"
    DELAY = "DELAYED"
    NONE = "NOT_FOUND"
    AUTH = "NOT_AUTHORIZED"

class StopGeneration(BaseModel):
    result: str = Gemini.Const.Stop()

class RestResultPoly(BaseModel):
    request_id: Optional[str] = None
    count: Optional[int] = None
    next_url: Optional[str] = None
    status: RestStatus  

class MarketSession(Enum):
    PRE = "pre-market"
    REG = "regular"
    POST = "post-market"
    CLOSED = "closed"
    NA = "not applicable"

class MarketEvent(Enum):
    PRE_OPEN = 0
    REG_OPEN = 1
    REG_CLOSE = 2
    POST_CLOSE = 3
    LAST_CLOSE = 4

class AssetClass(Enum):
    STOCKS = "stocks"
    OPTION = "options"
    CRYPTO = "crypto"
    FOREX = "fx"
    INDEX = "indices"
    OTC = "otc"

class SymbolType(Enum):
    COMMON = "Common Stock"
    ETP = "ETP"
    ADR = "ADR"
    REIT = "REIT"
    DELISTED = ""
    CEF = "Closed-End Fund"
    UNIT = "Unit"
    RIGHT = "Right"
    EQUITY = "Equity WRT"
    GDR = "GDR"
    PREF = "Preference"
    CDI = "CDI"
    NVDR = "NVDR"
    REG = "NY Reg Shrs"
    MLP = "MLP"
    MUTUAL = "Mutual Fund"

class Locale(Enum):
    US = "us"
    GLOBAL = "global"

class Sentiment(Enum):
    V_POS = "very positive"
    POSITIVE = "positive"
    NEUTRAL_P = "neutral/positive"
    NEUTRAL_SP = "neutral/slightly positive"
    NEUTRAL = "neutral"
    NEUTRAL_SN = "neutral/slightly negative"
    NEUTRAL_N = "neutral/negative"
    MIXED = "mixed"
    NEGATIVE = "negative"
    V_NEG = "very negative"

class Trend(Enum):
    S_BUY = "strong-buy"
    BUY = "buy"
    HOLD = "hold"
    SELL = "sell"
    S_SELL = "strong-sell"

class MarketCondition(Enum):
    BULL = "bullish"
    BULLN = "cautiously bullish"
    HOLD = "hold"
    BEARN = "cautiously bearish"
    BEAR = "bearish"

class GeneratedEvent(BaseModel):
    last_close: str
    pre_open: str
    reg_open: str
    reg_close: str
    post_close: str
    timestamp: Optional[str] = None
    is_holiday: Optional[bool] = None

    def model_post_init(self, *args, **kwargs) -> None:
        if self.timestamp is None:
            self.timestamp = datetime.now(self.tz()).strftime('%c')
        if self.is_holiday is None:
            self.is_holiday = False

    def session(self, with_date: Optional[str] = None) -> MarketSession:
        if with_date is None:
            with_date = datetime.now(self.tz()).strftime('%c')
        compare = parse(with_date)
        if self.is_holiday or compare.weekday() > 4: # weekend
            return MarketSession.CLOSED
        events = [parse(event).time() for event in [self.pre_open,self.reg_open,self.reg_close,self.post_close]]
        if compare.time() < events[0]:
            return MarketSession.CLOSED
        else:
            session = MarketSession.NA
            if compare.time() >= events[0]:
                session = MarketSession.PRE
            if compare.time() >= events[1]:
                session = MarketSession.REG
            if compare.time() >= events[2]:
                session = MarketSession.POST
            if compare.time() >= events[3]:
                session = MarketSession.CLOSED
        return session

    def is_open(self) -> bool:
        return self.session() != MarketSession.CLOSED

    def has_update(self) -> bool:
        datetime_now = datetime.now(self.tz())
        self_ts = parse(self.timestamp)
        # Re-generate events for a new day.
        if datetime_now.day > self_ts.day:
            return True
        # No updates on holidays or when generated after post_close.
        if self.is_holiday or self_ts.time() >= parse(self.post_close).time():
            return False
        # Compare current time to generated event times.
        for event in [self.pre_open,self.reg_open,self.reg_close]:
            if datetime_now.time() > parse(event).time():
                return True
        # Current time is before pre_open.
        return False

    @classmethod
    def tz(cls):
        return pytz.timezone('US/Eastern') # Exchanges data is in eastern time.
    
    @classmethod
    def apply_fix(cls, value, fix: datetime) -> tuple[str, datetime]:
        api.validation_fail()
        value = fix.strftime('%c')
        return value, fix
    
    @field_validator("last_close")
    def valid_close(cls, value):
        date_gen = parse(value) # Generated close is in eastern time and tzinfo naive.
        date_now = parse(datetime.now(cls.tz()).strftime('%c')) # Need now in same format as generated.
        # Soft-pass: when actual session is closed after post-market
        if date_now.day == date_gen.day+1 and date_now.weekday() <= 4:
            date_fix = date_gen.replace(day=date_now.day)
            if date_fix.timestamp() < date_now.timestamp():
                value, date_gen = cls.apply_fix(value, date_fix) # soft-pass: use today's close
        # Soft-pass: when actual session is open post-market
        if date_now.day == date_gen.day and date_now.timestamp() < date_gen.timestamp():
            if date_now.weekday() > 0:
                date_fix = date_gen.replace(day=date_now.day-1)
            else:
                date_fix = date_gen.replace(day=date_now.day-3)
            if date_now.timestamp() > date_fix.timestamp():
                value, date_gen = cls.apply_fix(value, date_fix) # soft-pass: use previous close
        if date_now.weekday() == 0 or date_now.weekday() == 1 and date_gen.weekday() <= 4: # 0=monday, 4=friday
            return value # pass: generated thurs/friday on a monday/tues
        elif date_now.weekday() > 0 and date_now.weekday() <= 4 and date_gen.weekday() <= date_now.weekday()-1:
            return value # pass: generated yesterday/prior on a tues-fri
        elif date_now.weekday() > 4 and date_gen.weekday() <= 4:
            return value # pass: generated thurs/friday on a weekend
        elif date_now.day == date_gen.day and date_now.timestamp() > date_gen.timestamp():
            return value # pass: generated today after closed
        elif date_now.timestamp() < date_gen.timestamp():
            raise ValueError("last close cannot be a future value")
        else:
            raise ValueError("generated invalid last close")
        api.validation_fail()

class VectorStoreResult(BaseModel):
    docs: str
    dist: Optional[float] # requires query
    meta: Optional[dict]  # requires get or query
    store_id: str

class Aggregate(RestResultPoly):
    symbol: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    otc: Optional[bool] = None
    preMarket: Optional[float] = None
    afterHours: Optional[float] = None

class DailyCandle(Aggregate):
    from_date: str

class AggregateWindow(BaseModel):
    o: float
    h: float
    l: float
    c: float
    v: int # traded volume
    n: Optional[int] = None # transaction count
    vw: Optional[float] = None # volume weighted average price
    otc: Optional[bool] = None
    t: int

    @field_validator("t")
    def valid_t(cls, value):
        if not value > 0:
            raise ValueError("invalid timestamp")
        if len(str(value)) == 13:
            return int(value/1000)
        return value

class CustomCandle(RestResultPoly): 
    ticker: str
    adjusted: bool
    queryCount: int
    resultsCount: int
    results: list[AggregateWindow]

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[AggregateWindow]:
        return self.results
    
class MarketStatus(BaseModel):
    exchange: str
    holiday: Optional[str] = None
    isOpen: bool
    session: Optional[MarketSession] = None
    t: int
    timezone: str

    def model_post_init(self, *args, **kwargs) -> None:
        if self.session is None:
            self.session = MarketSession.CLOSED
        if self.holiday is None:
            self.holiday = MarketSession.NA.value

class MarketStatusResult(BaseModel):
    results: MarketStatus

    def get(self) -> MarketStatus:
        return self.results

class Symbol(BaseModel):
    description: str
    displaySymbol: str
    symbol: str
    type: SymbolType

class SymbolResult(BaseModel):
    count: int
    result: list[Symbol]

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.result)

    def get(self) -> list[Symbol]:
        return self.result

class Quote(BaseModel):
    c: float
    d: float
    dp: float
    h: float
    l: float
    o: float
    pc: float
    t: int

    @field_validator("t")
    def valid_t(cls, value):
        if not value > 0:
            raise ValueError("invalid timestamp")
        return value

class PeersResult(BaseModel):
    results: list[str]
    count: Optional[int] = None

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[str]:
        return self.results

class BasicFinancials(BaseModel):
    metric: dict
    metricType: str
    series: dict
    symbol: str

class Insight(BaseModel):
    sentiment: Sentiment|MarketCondition
    sentiment_reasoning: str
    ticker: str

class Publisher(BaseModel):
    favicon_url: Optional[str]
    homepage_url: str
    logo_url: str
    name: str

class NewsSummary(BaseModel):
    title: str
    summary: Optional[str]
    insights: Optional[list[Insight]]
    published_utc: str

class NewsTypePoly(BaseModel):
    amp_url: Optional[str] = None
    article_url: str
    title: str
    author: str
    description: Optional[str] = None
    id: str
    image_url: Optional[str] = None
    insights: Optional[list[Insight]] = None
    keywords: Optional[list[str]] = None
    published_utc: str
    publisher: Publisher
    tickers: list[str]

    def summary(self):
        return NewsSummary(title=self.title,
                           summary=self.description,
                           insights=self.insights,
                           published_utc=self.published_utc)

class NewsResultPoly(RestResultPoly):
    results: list[NewsTypePoly]

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[NewsTypePoly]:
        return self.results

class NewsTypeFinn(BaseModel):
    category: str
    datetime: int
    headline: str
    id: int
    image: str
    related: str # symbol
    source: str
    summary: str
    url: str

    def summary(self):
        return NewsSummary(title=self.headline,
                           summary=self.summary,
                           insights=None,
                           published_utc=self.datetime)

class NewsResultFinn(BaseModel):
    results: list[NewsTypeFinn]
    count: Optional[int] = None

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[NewsTypeFinn]:
        return self.results

class NewsTypeGenerated(BaseModel):
    title: str
    summary: str
    insights: list[Insight]
    keywords: list[str]
    source: Publisher
    published_utc: str
    tickers: list[str]
    url: str

    def summary(self):
        return NewsSummary(title=self.title,
                           summary=self.summary,
                           insights=self.insights,
                           published_utc=self.published_utc)

class TickerOverview(BaseModel):
    ticker: str
    name: str
    market: AssetClass
    locale: Locale
    primary_exchange: Optional[str] = None
    active: bool
    currency_name: str
    cik: Optional[str] = None
    composite_figi: Optional[str] = None
    share_class_figi: Optional[str] = None
    market_cap: Optional[int|float] = None
    phone_number: Optional[str] = None
    address: Optional[dict] = None
    description: Optional[str] = None
    sic_code: Optional[str] = None
    sic_description: Optional[str] = None
    ticker_root: Optional[str] = None
    homepage_url: Optional[str] = None
    total_employees: Optional[int] = None
    list_date: Optional[str] = None
    branding: Optional[dict] = None
    share_class_shares_outstanding: Optional[int] = None
    weighted_shares_outstanding: Optional[int] = None
    round_lot: Optional[int] = None

class OverviewResult(RestResultPoly):
    results: TickerOverview

    def get(self) -> TickerOverview:
        return self.results

class RecommendationTrend(BaseModel):
    buy: int
    hold: int
    period: str
    sell: int
    strongBuy: int
    strongSell: int
    symbol: str

class TrendsResult(BaseModel):
    results: list[RecommendationTrend]
    count: Optional[int] = None

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[RecommendationTrend]:
        return self.results
```

## Contents Memory


```python
# A contents-memory object.
class Memory:
    def __init__(self):
        self.system = f"""Give a concise, and detailed summary. Use information that you learn from the API responses.
        Use your tools and function calls according to the rules. Convert any all-upper case identifiers
        to proper case in your response. Convert any abbreviated or shortened identifiers to their full forms.
        Convert timestamps according to the rules before including them. Think step by step.
        """
        self.revery = {}
        self.prompt = None
        self.summary = None
    
    def set_prompt(self, prompt):
        self.prompt = f"""
        The current date and time is: {datetime.now(GeneratedEvent.tz()).strftime('%c')}
        
        {prompt}
        """
        self.contents = [types.Content(role="user", parts=[types.Part(text=self.prompt)])]

    def set_reason(self, step):
        # Append the model's reasoning part.
        self.contents.append(types.Content(role="model", parts=[types.Part(thought=True,text=step)]))

    def append_code(self, prompt, code_response_parts):
        subroutine_content = [types.Content(role="user", parts=[types.Part(text=prompt)]),
                              types.Content(role="model", parts=code_response_parts)]
        # Append the model's generated code and execution result.
        self.revery[datetime.now(GeneratedEvent.tz()).strftime('%c')] = { 
            "contents": subroutine_content
        }

    def update_contents(self, function_call, api_response_part):
        # Append the model's function call part.
        self.contents.append(types.Content(role="model", parts=[types.Part(function_call=function_call)])) 
        # Append the api response part.
        self.contents.append(types.Content(role="user", parts=[api_response_part]))

    def set_summary(self, summary):
        self.summary = summary
        self.contents.append(types.Content(role="model", parts=[types.Part(text=summary)]))
        self.revery[datetime.now(GeneratedEvent.tz()).strftime('%c')] = {
            "prompt": self.prompt, 
            "summary": self.summary, 
            "contents": self.contents
        }
        self.contents = None

memory = Memory()
```

## Retrieval-Augmented Generation


```python
# Define tool: retrieval-augmented generation.
# - using Chroma and text-embedding-004 for storage and retrieval
# - using gemini-2.0-flash for augmented generation
class RetrievalAugmentedGenerator:
    chroma_client = chromadb.PersistentClient(path="vector_db")
    config_temp = types.GenerateContentConfig(temperature=0.0)
    exchange_codes: Optional[dict] = None
    exchange_lists: dict = {}
    events: dict = {}
    holidays: dict = {}

    def __init__(self, genai_client, collection_name):
        self.client = genai_client
        self.embed_fn = GeminiEmbedFunction(genai_client)
        self.db = self.chroma_client.get_or_create_collection(
            name=collection_name, 
            embedding_function=self.embed_fn,  # type: ignore
            metadata={"hnsw:space": "cosine"})
        logging.getLogger("chromadb").setLevel(logging.ERROR) # suppress warning on existing id
        self.set_holidays("US", ["09-01-2025","10-13-2025","11-11-2025","11-27-2025","12-25-2025"])
        self.generated_events("US")

    def set_holidays(self, exchange_code: str, holidays: list):
        self.holidays[exchange_code] = [datetime.strptime(h, "%m-%d-%Y").date() for h in holidays]

    def get_exchange_codes(self, with_query: Optional[str] = None):
        gen = None
        if with_query and with_query not in self.exchange_lists.keys():
            gen = tqdm(total=1, desc="Generate exchange codes with_query")
            data = self.get_exchanges_csv(
                f"""What is the {with_query} exchange code? Return only the exchange codes 
                as a list in string form. Just the list string. 
                Omit all other information or details. Do not chat or use sentences.""").candidates[0].content
            self.exchange_lists[with_query] = ast.literal_eval(data.parts[-1].text)
        elif with_query is None and self.exchange_codes is None:
            gen = tqdm(total=1, desc="Generate exchange codes")
            data = self.get_exchanges_csv(
                """Give me a dictionary in string form. It must contain key:value pairs 
                mapping exchange code to name. Just the dictionary string. 
                Omit all other information or details. Do not chat or use sentences.""").candidates[0].content
            self.exchange_codes = ast.literal_eval(data.parts[-1].text.strip("\\`"))
        if gen:
            gen.update(1)
        return self.exchange_lists[with_query] if with_query else self.exchange_codes

    def get_event_date(self, event_t: str, exchange_code: str, event: MarketEvent):
        current_dt_str = datetime.now(GeneratedEvent.tz()).strftime('%c')
        current_dt = datetime.strptime(current_dt_str, "%a %b %d %H:%M:%S %Y")
        current_t_str = datetime.now(GeneratedEvent.tz()).strftime('%H:%M:%S')
        current_t = datetime.strptime(current_t_str, "%H:%M:%S").time()
        event_time = parse(event_t).time()
        gen_datetime = None
        if event is MarketEvent.LAST_CLOSE:
            last_close_day = current_dt.date() - timedelta(days=0 if current_t > event_time else 1)
            # Loop backwards to find the last valid trading day (not a weekend or holiday).
            while last_close_day.weekday() >= 5 or last_close_day in self.holidays[exchange_code]: # 5 = Sat, 6 = Sun
                last_close_day -= timedelta(days=1)
            # Combine the date and time.
            gen_datetime = datetime.combine(last_close_day, event_time)
        else:
            next_event_day = current_dt.date() + timedelta(days=0 if current_t < event_time else 1)
            # Loop forward to find the next valid trading day (not a weekend or holiday).
            while next_event_day.weekday() >= 5 or next_event_day in self.holidays[exchange_code]: # 5 = Sat, 6 = Sun
                next_event_day += timedelta(days=1)
            # Combine date and time.
            gen_datetime = datetime.combine(next_event_day, event_time)
        # Format the result as requested.
        return gen_datetime.strftime('%a %b %d %X %Y')

    def generate_event(self, exchange_code: str, event: MarketEvent):
        if event is MarketEvent.LAST_CLOSE or event is MarketEvent.POST_CLOSE:
            prompt = f"""What is the closing time including post_market hours."""
        elif event is MarketEvent.PRE_OPEN or event is MarketEvent.REG_OPEN:
            is_pre = "including" if event is MarketEvent.PRE_OPEN else "excluding"
            prompt = f"""What is the opening time {is_pre} pre_market hours."""
        elif event is MarketEvent.REG_CLOSE:
            prompt = f"""What is the closing time excluding post_market hours."""
        prompt = f"""Answer based on your knowledge of exchange operating hours.
            Do not answer in full sentences. Omit all chat and provide the answer only.
            The fields pre_market and post_market both represent extended operating hours.

            The current date and time: {datetime.now(GeneratedEvent.tz()).strftime('%c')}
            
            Consider the {exchange_code} exchange's operating hours.
            {prompt}
            
            Answer with the time in this format: '%H:%M:%S'.
            Omit all other chat and details. Do not use sentences."""
        progress = tqdm(total=1, desc=f"Generate {exchange_code}->{event}")
        response = self.get_exchanges_csv(prompt).candidates[0].content
        if api.Const.Stop() in f"{response.parts[-1].text}":
            progress.close()
            api.generation_fail()
            time.sleep(api.dt_between)
            return self.generate_event(exchange_code, event)
        else:
            response = self.get_event_date(response.parts[-1].text, exchange_code, event)
            progress.update(1)
            return response

    def generated_events(self, exchange_code: str) -> GeneratedEvent:
        # Check for an existing GeneratedEvent object having updates.
        if exchange_code in self.events.keys() and self.events[exchange_code].has_update():
            event_obj = self.events[exchange_code]
            event_state = [(event_obj.pre_open, MarketEvent.PRE_OPEN),
                           (event_obj.reg_open, MarketEvent.REG_OPEN),
                           (event_obj.reg_close, MarketEvent.REG_CLOSE),
                           (event_obj.post_close, MarketEvent.POST_CLOSE)]
            # Need now in same format as generated.
            datetime_now = parse(datetime.now(event_obj.tz()).strftime('%c'))
            gen_ts = parse(event_obj.timestamp)
            # Re-generate events when day changes.
            if datetime_now.day > gen_ts.day:
                del self.events[exchange_code]
                return self.generated_events(exchange_code)
            # Update changed events on trading days.
            for e in event_state:
                if datetime_now > parse(e[0]):
                    event_dt = self.generate_event(exchange_code, e[1])
                    match e[1]:
                        case MarketEvent.PRE_OPEN:
                            event_obj.pre_open = event_dt
                        case MarketEvent.REG_OPEN:
                            event_obj.reg_open = event_dt
                        case MarketEvent.REG_CLOSE:
                            event_obj.reg_close = event_dt
                        case MarketEvent.POST_CLOSE:
                            event_obj.post_close = event_dt
            event_obj.timestamp = datetime.now(event_obj.tz()).strftime('%c')
            self.events[exchange_code] = event_obj
        # Generate events for an exchange code not in cache.
        elif exchange_code not in self.events.keys():
            self.events[exchange_code] = GeneratedEvent(
                last_close=self.generate_event(exchange_code, MarketEvent.LAST_CLOSE),
                pre_open=self.generate_event(exchange_code, MarketEvent.PRE_OPEN),
                reg_open=self.generate_event(exchange_code, MarketEvent.REG_OPEN),
                reg_close=self.generate_event(exchange_code, MarketEvent.REG_CLOSE),
                post_close=self.generate_event(exchange_code, MarketEvent.POST_CLOSE),
                is_holiday=datetime.now().date() in self.holidays[exchange_code])
        return self.events[exchange_code]

    def set_holiday_event(self, exchange_code: str):
        self.generated_events(exchange_code).is_holiday = True

    def last_market_close(self, exchange_code: str):
        return self.generated_events(exchange_code).last_close

    def add_documents_list(self, docs: list):
        self.embed_fn.document_mode = True # Switch to document mode.
        ids = list(map(str, range(self.db.count(), self.db.count()+len(docs))))
        metas=[{"source": doc.metadata["source"]} for doc in docs]
        content=[doc.page_content for doc in docs]
        tqdm(self.db.add(ids=ids, documents=content, metadatas=metas), desc="Generate document embedding")

    def add_api_document(self, query: str, api_response: str, topic: str, source: str = "add_api_document"):
        self.embed_fn.document_mode = True # Switch to document mode.
        splitter = RecursiveJsonSplitter(max_chunk_size=Gemini.Const.ChunkMax())
        docs = splitter.create_documents(texts=[api_response], convert_lists=True)
        ids = list(map(str, range(self.db.count(), self.db.count()+len(docs))))
        content = [json.dumps(doc.page_content) for doc in docs]
        metas = [{"source": source, "topic": topic}]*len(docs)
        tqdm(self.db.add(ids=ids, documents=content, metadatas=metas), desc="Generate api embedding")

    def add_peers_document(self, query: str, names: list, topic: str, source: str, group: str):
        self.embed_fn.document_mode = True # Switch to document mode.
        peers = {"symbol": topic, "peers": names}
        tqdm(self.db.add(ids=str(self.db.count()),
                         documents=[json.dumps(peers)],
                         metadatas=[{"source": source, "topic": topic, "group": group}]),
             desc="Generate peers embedding")

    def get_peers_document(self, query: str, topic: str, group: str):
        return self.get_documents_list(query, where={"$and": [{"group": group}, {"topic": topic}]})

    def add_rest_chunks(self, chunks: list, topic: str, source: str, ids: Optional[list[str]] = None,
                        meta_opt: Optional[list[dict]] = None, is_update: bool = True):
        self.embed_fn.document_mode = True # Switch to document mode
        if ids is None:
            ids = list(map(str, range(self.db.count(), self.db.count()+len(chunks))))
        if isinstance(chunks[0], BaseModel):
            docs = [model.model_dump_json() for model in chunks]
        else:
            docs = [json.dumps(obj) for obj in chunks]
        meta_base = {"source": source, "topic": topic}
        if meta_opt is not None:
            for m in meta_opt:
                m.update(meta_base)
        metas = [meta_base]*len(chunks) if meta_opt is None else meta_opt
        if is_update:
            tqdm(self.db.upsert(ids=ids, documents=docs, metadatas=metas), desc="Upsert chunks embedding")
        else:
            tqdm(self.db.add(ids=ids, documents=docs, metadatas=metas), desc="Add chunks embedding")

    def get_market_status(self, exchange_code: str) -> tuple[list[VectorStoreResult], bool]: # result, has rest update
        self.embed_fn.document_mode = False # Switch to query mode.
        stored = self.stored_result(self.db.get(where={
            "$and": [{"exchange": exchange_code}, {"topic": "market_status"}]}))
        if len(stored) == 0:
            return stored, True
        # Check for a daily market status update.
        status = json.loads(stored[0].docs)
        gen_day = parse(self.generated_events(exchange_code).timestamp).day
        store_day = parse(stored[0].meta['timestamp']).day
        if status["holiday"] != MarketSession.NA.value and gen_day == store_day:
            return stored, False
        elif gen_day > store_day:
            return stored, True
        # Update with generated events to avoid rest api requests.
        status["session"] = self.generated_events(exchange_code).session().value
        status["isOpen"] = self.generated_events(exchange_code).is_open()
        stored[0].docs = json.dumps(status)
        return stored, False

    def get_basic_financials(self, query: str, topic: str, source: str = "get_financials_1"):
        return self.get_documents_list(
            query, max_sources=200, where={"$and": [{"source": source}, {"topic": topic}]})

    def add_quote_document(self, query: str, quote: str, topic: str, timestamp: int, source: str):
        self.embed_fn.document_mode = True # Switch to document mode.
        tqdm(self.db.add(ids=str(self.db.count()), 
                             documents=[quote], 
                             metadatas=[{"source": source, "topic": topic, "timestamp": timestamp}]), 
             desc="Generate quote embedding")

    def get_api_documents(self, query: str, topic: str, source: str = "add_api_document", 
                          meta_opt: Optional[list[dict]] = None):
        where = [{"source": source}, {"topic": topic}]
        if meta_opt is None:
            return self.get_documents_list(query, where={"$and": where})
        else:
            for meta in meta_opt:
                for k,v in meta.items():
                    where.append({k: v})
            return self.get_documents_list(query, where={"$and": where})

    def query_api_documents(self, query: str, topic: str, source: str = "add_api_document"):
        return self.generate_answer(query, where={"$and": [{"source": source}, {"topic": topic}]})

    def add_grounded_document(self, query: str, topic: str, result):
        self.embed_fn.document_mode = True # Switch to document mode.
        chunks = result.candidates[0].grounding_metadata.grounding_chunks
        supports = result.candidates[0].grounding_metadata.grounding_supports
        if supports is not None: # Only add grounded documents which have supports
            grounded_text = [f"{s.segment.text}" for s in supports]
            source = [f"{c.web.title}" for c in chunks]
            score = [f"{s.confidence_scores}" for s in supports]
            tqdm(self.db.add(ids=str(self.db.count()),
                             documents=json.dumps(grounded_text),
                             metadatas=[{"source": ", ".join(source),
                                         "confidence_score": ", ".join(score),
                                         "topic": topic,
                                         "question": query}]),
                 desc="Generate grounding embedding")

    def get_grounding_documents(self, query: str, topic: str):
        self.embed_fn.document_mode = False # Switch to query mode.
        return self.stored_result(self.db.get(where={"$and": [{"question": query}, {"topic": topic}]}))
            
    def add_wiki_documents(self, title: str, wiki_chunks: list):
        self.embed_fn.document_mode = True # Switch to document mode.
        result = self.get_wiki_documents(title)
        if len(result) == 0:
            ids = list(map(str, range(self.db.count(), self.db.count()+len(wiki_chunks))))
            metas=[{"title": title, "source": "add_wiki_documents"}]*len(wiki_chunks)
            tqdm(self.db.add(ids=ids, documents=wiki_chunks, metadatas=metas), desc="Generate wiki embeddings")

    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def generate_with_wiki_passages(self, query: str, title: str, passages: list[str]):
        return self.generate_answer(query, where={"title": title}, passages=passages)
    
    def get_wiki_documents(self, title: Optional[str] = None):
        self.embed_fn.document_mode = False # Switch to query mode.
        if title is None:
            return self.stored_result(self.db.get(where={"source": "add_wiki_document"}))
        else:
            return self.stored_result(self.db.get(where={"title": title}))

    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def get_documents_list(self, query: str, max_sources: int = 5000, where: Optional[dict] = None):
        self.embed_fn.document_mode = False # Switch to query mode.
        return self.stored_result(
            self.db.query(query_texts=[query], 
                          n_results=max_sources, 
                          where=where), 
            is_query = True)

    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def get_exchanges_csv(self, query: str):
        return self.generate_answer(query, max_sources=100, where={"source": "exchanges.csv"})

    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def generate_answer(self, query: str, max_sources: int = 10, 
                        where: Optional[dict] = None, passages: Optional[list[str]] = None):
        stored = self.get_documents_list(query, max_sources, where)
        query_oneline = query.replace("\n", " ")
        prompt = f"""You're an expert writer. You understand how to interpret html and markdown. You will accept the
        question below and answer based only on the passages. Never mention the passages in your answers. Be sure to 
        respond in concise sentences. Include all relevant background information when possible. If a passage is not 
        relevant to the answer you must ignore it. If no passage answers the question respond with: I don't know.

        QUESTION: {query_oneline}
        
        """
        # Add the retrieved documents to the prompt.
        stored_docs = [passage.docs for passage in stored]
        for passage in stored_docs if passages is None else stored_docs + passages:
            passage_oneline = passage.replace("\n", " ")
            prompt += f"PASSAGE: {passage_oneline}\n"
        # Generate the response.
        response = api.retriable(
            self.client.models.generate_content,
            model=api(Gemini.Model.GEN),
            config=self.config_temp,
            contents=prompt)
        # Check for generated code and store in memory.
        content = response.candidates[0].content
        if len(content.parts) > 1 and content.parts[0].executable_code:
            memory.append_code(prompt, content.parts)
        return response

    def stored_result(self, result, is_query: bool = False) -> list[VectorStoreResult]:
        try:
            results = []
            if len(result["documents"]) == 0:
                return results
            if isinstance(result["documents"][0], list):
                for i in range(len(result["documents"][0])):
                    obj = VectorStoreResult(docs=result["documents"][0][i],
                                            dist=result["distances"][0][i] if is_query else None,
                                            meta=result["metadatas"][0][i],
                                            store_id=result["ids"][0][i])
                    results.append(obj)
            else:
                results.append(
                    VectorStoreResult(docs=result["documents"][0],
                                      dist=result["distances"][0] if is_query else None,
                                      meta=result["metadatas"][0],
                                      store_id=result["ids"][0]))
            return results
        except Exception as e:
            raise e
```

## Wiki Grounding


```python
# Define tool: wiki-grounding generation.
# - using gemini-2.0-flash for response generation
# - using a RAG-implementation to store groundings
# - create new groundings by similarity to topic
# - retrieve existing groundings by similarity to topic
class WikiGroundingGenerator:   
    def __init__(self, genai_client, rag_impl):
        self.client = genai_client
        self.rag = rag_impl
        with warnings.catch_warnings():
            warnings.simplefilter("ignore") # suppress beta-warning
            self.splitter = HTMLSemanticPreservingSplitter(
                headers_to_split_on=[("h2", "Main Topic"), ("h3", "Sub Topic")],
                separators=["\n\n", "\n", ". ", "! ", "? "],
                max_chunk_size=Gemini.Const.ChunkMax(),
                chunk_overlap=50,
                preserve_links=True,
                preserve_images=True,
                preserve_videos=True,
                preserve_audio=True,
                elements_to_preserve=["table", "ul", "ol", "code"],
                denylist_tags=["script", "style", "head"],
                custom_handlers={"code": self.code_handler},
            )

    def generate_answer(self, query: str, topic: str):
        stored = self.rag.get_wiki_documents(topic)
        if len(stored) > 0:
            return self.rag.generate_with_wiki_passages(query, topic, [chunk.docs for chunk in stored]).text
        else:
            pages = wikipedia.search(topic + " company")
            if len(pages) > 0:
                p_topic_match = 0.80
                for i in range(len(pages)):
                    if tqdm(api.similarity([topic + " company", pages[i]]) > p_topic_match, 
                            desc= "Score wiki search by similarity to topic"):
                        page_html = api.get(f"https://en.wikipedia.org/wiki/{pages[i]}")
                        chunks = [chunk.page_content for chunk in self.splitter.split_text(page_html)]
                        self.rag.add_wiki_documents(topic, chunks)
                        return self.rag.generate_with_wiki_passages(query, topic, chunks).text
            return StopGeneration().result

    def code_handler(self, element: Tag) -> str:
        data_lang = element.get("data-lang")
        code_format = f"<code:{data_lang}>{element.get_text()}</code>"
        return code_format
```

## Search Grounding


```python
# Define tool: search-grounding generation.
# - using gemini-2.0-flash with GoogleSearch tool for response generation
# - using a RAG-implementation to store groundings
# - create new groundings by exact match to topic
# - retrieve existing groundings by similarity to topic
class SearchGroundingGenerator:
    config_ground = types.GenerateContentConfig(
        tools=[types.Tool(google_search=types.GoogleSearch())],
        temperature=0.0
    )
    
    def __init__(self, genai_client, rag_impl):
        self.client = genai_client
        self.rag = rag_impl

    def generate_answer(self, query: str, topic: str):
        stored = self.rag.get_grounding_documents(query, topic)
        if len(stored) > 0:
            for i in range(len(stored)):
                meta_q = stored[i].meta["question"]
                p_ground_match = 0.95 # This can be really high ~ 95-97%
                if tqdm(api.similarity([query, meta_q]) > p_ground_match,
                        desc="Score similarity to stored grounding"):
                    return ast.literal_eval(stored[i].docs)
        return self.get_grounding(query, topic)

    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def get_grounding(self, query: str, topic: str):
        contents = [types.Content(role="user", parts=[types.Part(text=query)])]
        contents += f"""
        You're a search assistant that provides grounded answers to questions about {topic}. You will provide only 
        results that discuss {topic}. Be brief and specific in answering and omit extra details.
        If an answer is not possible respond with: I don't know."""
        response = api.retriable(self.client.models.generate_content, 
                                 model=api(Gemini.Model.GEN), 
                                 config=self.config_ground, 
                                 contents=contents)
        if response.candidates[0].grounding_metadata.grounding_supports is not None:
            if self.is_consistent(query, topic, response.text):
                self.rag.add_grounded_document(query, topic, response)
                return response.text 
        return StopGeneration().result # Empty grounding supports or not consistent in response

    def is_consistent(self, query: str, topic: str, model_response: str) -> bool:
        topic = topic.replace("'", "")
        id_strs = topic.split()
        if len(id_strs) == 1:
            matches = re.findall(rf"{id_strs[0]}[\s,.]+\S+", query)
            if len(matches) > 0:
                topic = matches[0]
        compound_match = re.findall(rf"{id_strs[0]}[\s,.]+\S+", model_response)
        model_response = model_response.replace("'", "")
        if len(compound_match) == 0 and topic in model_response:
            return True # not a compound topic id and exact topic match
        for match in compound_match:
            if topic not in match:
                return False
        return True # all prefix matches contained topic
```

## Rest Grounding


```python
# Rest api-helpers to manage request-per-minute limits.
# - define an entry for each endpoint limit
# - init rest tool with limits to create blocking queues
# - apply a limit to requests with rest_tool.try_url
class ApiLimit(Enum):
    FINN = "finnhub.io",50
    POLY = "polygon.io",4 # (id_url,rpm)

class BlockingUrlQueue:
    on_cooldown = False
    cooldown = None
    cooldown_start = None
    
    def __init__(self, rest_fn: Callable, per_minute: int):
        self.per_minute_max = per_minute
        self.quota = per_minute
        self.rest_fn = rest_fn

    def push(self, rest_url: str):
        if not self.on_cooldown:
            self.cooldown = Timer(60, self.reset_quota)
            self.cooldown.start()
            self.cooldown_start = time.time()
            self.on_cooldown = True
        if self.quota > 0:
            self.quota -= 1
            time.sleep(0.034) # ~30 requests per second
            return self.rest_fn(rest_url)
        else:
            print(f"limited {self.per_minute_max}/min, waiting {self.limit_expiry()}s")
            time.sleep(max(self.limit_expiry(),0.5))
            return self.push(rest_url)

    def reset_quota(self):
        self.quota = self.per_minute_max
        self.on_cooldown = False
        self.cooldown_start = None

    def limit_expiry(self):
        if self.cooldown_start:
            return max(60-(time.time()-self.cooldown_start),0)
        return 0
```


```python
# Define tool: rest-grounding generation.
# - using gemini-2.0-flash for response generation
# - using a RAG-implementation to store groundings
# - reduce long-context by chunked pre-processing
class RestGroundingGenerator:    
    limits = None

    def __init__(self, rag_impl, with_limits: bool):
        self.rag = rag_impl
        if with_limits:
            self.limits = {}
            for rest_api in ApiLimit:
                self.limits[rest_api.value[0]] = BlockingUrlQueue(api.get, rest_api.value[1])

    def get_limit(self, rest_api: ApiLimit) -> Optional[BlockingUrlQueue]:
        return self.limits[rest_api.value[0]] if self.limits else None

    def basemodel(self, data: str, schema: BaseModel, from_lambda: bool = False) -> Optional[BaseModel]:
        try:
            if from_lambda:
                return schema(results=json.loads(data))
            return schema.model_validate_json(data)
        except Exception as e:
            raise e

    def dailycandle(self, data: str) -> Optional[DailyCandle]:
        try:
            candle = json.loads(data)
            if "from" not in candle:
                raise ValueError("not a dailycandle / missing value for date")
            agg = self.basemodel(data, Aggregate)
            return DailyCandle(from_date=candle["from"], 
                               status=agg.status.value, 
                               symbol=agg.symbol, 
                               open=agg.open, 
                               high=agg.high, 
                               low=agg.low, 
                               close=agg.close, 
                               volume=agg.volume, 
                               otc=agg.otc, 
                               preMarket=agg.preMarket, 
                               afterHours=agg.afterHours)
        except Exception as e:
            raise e

    @retry.Retry(timeout=600)
    def try_url(self, url: str, schema: BaseModel, as_lambda: bool, with_limit: Optional[BlockingUrlQueue],
                success_fn: Callable, *args, **kwargs):
        try:
            if self.limits is None:
                data = api.get(url)
            elif with_limit:
                data = with_limit.push(url)
            if schema is DailyCandle:
                model = self.dailycandle(data)
            else:
                model = self.basemodel(data, schema, as_lambda)
        except Exception as e:
            try:
                print(f"try_url exception: {e}")
                if issubclass(schema, RestResultPoly):
                    return success_fn(*args, **kwargs, result=self.basemodel(data, RestResultPoly))
            except Exception as not_a_result:
                print(not_a_result)
            return StopGeneration()
        else:
            return success_fn(*args, **kwargs, model=model)

    def get_symbol_matches(self, with_content, by_name: bool, model: SymbolResult):
        matches = []
        max_failed_match = model.count if not by_name else 3
        p_desc_match = 0.92
        p_symb_match = 0.95
        if model.count > 0:
            for obj in tqdm(model.get(), desc="Score similarity to query"):
                if max_failed_match > 0:
                    desc = [with_content["q"].upper(), obj.description.split("-", -1)[0]]
                    symb = [with_content["q"].upper(), obj.symbol]
                    if by_name and api.similarity(desc) > p_desc_match: 
                        matches.append(obj.symbol)
                    elif not by_name and api.similarity(symb) > p_symb_match:
                        matches.append(obj.description)
                        max_failed_match = 0
                    else:
                        max_failed_match -= 1
        if len(matches) > 0:
            self.rag.add_api_document(with_content["query"], matches, with_content["q"], "get_symbol_1")
            return matches
        return StopGeneration().result

    def get_quote(self, with_content, model: Quote):
        quote = model.model_dump_json()
        self.rag.add_quote_document(with_content["query"], quote, with_content["symbol"], model.t, "get_quote_1")
        return quote

    def parse_financials(self, with_content, model: BasicFinancials):
        metric = list(model.metric.items())
        chunks = []
        # Chunk the metric data.
        for i in range(0, len(metric), Gemini.Const.MetricBatch()):
            batch = metric[i:i + Gemini.Const.MetricBatch()]
            chunks.append({"question": with_content["query"], "answer": batch})
        # Chunk the series data.
        for key in model.series.keys():
            series = list(model.series[key].items())
            for s in series:
                if api.token_count(s) <= Gemini.Const.ChunkMax():
                    chunks.append({"question": with_content["query"], "answer": s})
                else:
                    k = s[0]
                    v = s[1]
                    for i in range(0, len(v), Gemini.Const.SeriesBatch()):
                        batch = v[i:i + Gemini.Const.SeriesBatch()]
                        chunks.append({"question": with_content["query"], "answer": {k: batch}})
        self.rag.add_rest_chunks(chunks, topic=with_content["symbol"], source="get_financials_1")
        return chunks

    def parse_news(self, with_content, model: NewsResultFinn):
        if model.count > 0:
            metas = []
            for digest in model.get():
                pub_date = datetime.fromtimestamp(digest.datetime, tz=GeneratedEvent.tz()).strftime("%Y-%m-%d")
                metas.append({"publisher": digest.source,
                              "published_est": parse(pub_date).timestamp(),
                              "news_id": digest.id,
                              "related": digest.related})
            self.rag.add_rest_chunks(model.get(), topic=with_content["symbol"], source="get_news_1",
                                     ids=[f"{digest.id}+news" for digest in model.get()],
                                     meta_opt=metas, is_update=False)
            return [digest.summary().model_dump_json() for digest in model.get()]
        return StopGeneration().result

    def parse_news(self, with_content, model: Optional[NewsResultPoly] = None,
                   result: Optional[RestResultPoly] = None) -> tuple[list, str]: # list of summary, next list url
        if model and model.status in [RestStatus.OK, RestStatus.DELAY]:
            metas = []
            for news in model.get():
                pub_date = parse(news.published_utc).strftime("%Y-%m-%d")
                metas.append({"publisher": news.publisher.name,
                              "published_utc": parse(pub_date).timestamp(),
                              "news_id": news.id,
                              "related": json.dumps(news.tickers),
                              "keywords": json.dumps(news.keywords)})
            self.rag.add_rest_chunks(model.get(), topic=with_content["ticker"], source="get_news_2",
                                     ids=[news.id for news in model.get()],
                                     meta_opt=metas, is_update=False)
            return [news.summary().model_dump_json() for news in model.get()], model.next_url
        elif result:
            return result.model_dump_json()

    def parse_daily_candle(self, with_content, model: Optional[DailyCandle] = None,
                           result: Optional[RestResultPoly] = None):
        if model and model.status in [RestStatus.OK, RestStatus.DELAY]:
            self.rag.add_rest_chunks(
                chunks=[model],
                topic=with_content["stocksTicker"],
                source="daily_candle_2",
                meta_opt=[{"from_date": model.from_date, "adjusted": with_content["adjusted"]}])
            return model
        elif result:
            return result

    def parse_custom_candle(self, with_content, model: Optional[CustomCandle] = None,
                            result: Optional[RestResultPoly] = None):
        if model and model.status in [RestStatus.OK, RestStatus.DELAY]:
            metas = [{
                "timespan": with_content["timespan"],
                "adjusted": with_content["adjusted"],
                "from": with_content["from"],
                "to": with_content["to"]}]*model.count
            candles = [candle.model_dump_json() for candle in model.get()]
            self.rag.add_rest_chunks(
                chunks=candles,
                topic=with_content["stocksTicker"],
                source="custom_candle_2",
                meta_opt=metas)
            return candles
        elif result:
            return result.model_dump_json()

    def parse_overview(self, with_content, model: OverviewResult):
        overview = [model.get().model_dump_json()]
        self.rag.add_rest_chunks(chunks=overview, topic=with_content["ticker"], source="ticker_overview_2")
        return overview

    def parse_trends(self, with_content, model: TrendsResult):
        if model.count > 0:
            metas = [{"period": trend.period} for trend in model.get()]
            trends = [trend.model_dump_json() for trend in model.get()]
            self.rag.add_rest_chunks(trends, topic=with_content["symbol"], source="trends_1", meta_opt=metas)
            return trends
        return StopGeneration().result

    def augment_market_status(self, with_id: Optional[str], model: MarketStatusResult):
        if model.get().holiday != MarketSession.NA.value:
            self.rag.set_holiday_event(model.get().exchange)
        events = self.rag.generated_events(model.get().exchange)
        model.get().session = events.session()
        model.get().isOpen = events.is_open()
        meta = {"exchange": model.get().exchange,
                "last_close": events.last_close,
                "pre_open": events.pre_open,
                "reg_open": events.reg_open,
                "reg_close": events.reg_close,
                "post_close": events.post_close,
                "timestamp": events.timestamp }
        self.rag.add_rest_chunks([model.get()],
                                 topic="market_status",
                                 source="get_market_status_1",
                                 ids=[with_id] if with_id else None,
                                 meta_opt=[meta])
        return model.get().model_dump_json()

    def get_symbol(self, content, by_name: bool = True):
        return self.try_url(
            f"https://finnhub.io/api/v1/search?q={content['q']}&exchange={content['exchange']}&token={FINNHUB_API_KEY}",
            schema=SymbolResult,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.get_symbol_matches,
            with_content=content,
            by_name=by_name)

    def get_current_price(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/quote?symbol={content['symbol']}&token={FINNHUB_API_KEY}",
            schema=Quote,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.get_quote,
            with_content=content)

    def get_market_status(self, content, store_id: Optional[str] = None):
        return self.try_url(
            f"https://finnhub.io/api/v1/stock/market-status?exchange={content['exchange']}&token={FINNHUB_API_KEY}",
            schema=MarketStatusResult,
            as_lambda=True,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.augment_market_status,
            with_id=store_id)

    def get_peers(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/stock/peers?symbol={content['symbol']}&grouping={content['grouping']}&token={FINNHUB_API_KEY}",
            schema=PeersResult,
            as_lambda=True,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=lambda model: model)

    def get_basic_financials(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/stock/metric?symbol={content['symbol']}&metric={content['metric']}&token={FINNHUB_API_KEY}",
            schema=BasicFinancials,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.parse_financials,
            with_content=content)

    def get_news_simple(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/company-news?symbol={content['symbol']}&from={content['from']}&to={content['to']}&token={FINNHUB_API_KEY}",
            schema=NewsResultFinn,
            as_lambda=True,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.parse_news,
            with_content=content)

    def get_news_tagged(self, content):
        next_url = f"https://api.polygon.io/v2/reference/news?ticker={content['ticker']}&published_utc.gte={content['published_utc.gte']}&published_utc.lte={content['published_utc.lte']}&order={content['order']}&limit={content['limit']}&sort={content['sort']}&apiKey={POLYGON_API_KEY}"
        news = []
        while True:
            news_list, next_url = self.try_url(
                next_url,
                schema=NewsResultPoly,
                as_lambda=False,
                with_limit=self.get_limit(ApiLimit.POLY),
                success_fn=self.parse_news,
                with_content=content)
            news += news_list
            if next_url is None:
                break
            next_url += f"&apiKey={POLYGON_API_KEY}"
        return news

    def get_daily_candle(self, content):
        return self.try_url(
            f"https://api.polygon.io/v1/open-close/{content['stocksTicker']}/{content['date']}?adjusted={content['adjusted']}&apiKey={POLYGON_API_KEY}",
            schema=DailyCandle,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.POLY),
            success_fn=self.parse_daily_candle,
            with_content=content)

    def get_custom_candle(self, content):
        return self.try_url(
            f"https://api.polygon.io/v2/aggs/ticker/{content['stocksTicker']}/range/{content['multiplier']}/{content['timespan']}/{content['from']}/{content['to']}?adjusted={content['adjusted']}&sort={content['sort']}&limit={content['limit']}&apiKey={POLYGON_API_KEY}",
            schema=CustomCandle,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.POLY),
            success_fn=self.parse_custom_candle,
            with_content=content)

    def get_overview(self, content):
        return self.try_url(
            f"https://api.polygon.io/v3/reference/tickers/{content['ticker']}?apiKey={POLYGON_API_KEY}",
            schema=OverviewResult,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.POLY),
            success_fn=self.parse_overview,
            with_content=content)

    def get_trends_simple(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/stock/recommendation?symbol={content['symbol']}&token={FINNHUB_API_KEY}",
            schema=TrendsResult,
            as_lambda=True,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.parse_trends,
            with_content=content)
```

## Callable Functions


```python
# Callable functions in openapi schema.
decl_get_symbol_1 = types.FunctionDeclaration(
    name="get_symbol_1",
    description="""Search for the stock ticker symbol of a given company, security, isin or cusip. Each ticker
                   entry provides a description, symbol, and asset type. If this doesn't help you should try 
                   calling get_wiki_tool_response next.""",
    parameters={
        "type": "object",
        "properties": {
            "q": {
                "type": "string",
                "description": """The company, security, isin or cusip to search for a symbol."""
            },
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is 'US' for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["q", "exchange", "query"]
    }
)

decl_get_symbols_1 = types.FunctionDeclaration(
    name="get_symbols_1",
    description="""List all supported symbols and tickers. The results are filtered by exchange code.""",
    parameters={
        "type": "object",
        "properties": {
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter the results."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["exchange", "query"]
    }
)

decl_get_name_1 = types.FunctionDeclaration(
    name="get_name_1",
    description="""Search for the name associated with a stock ticker or symbol's company, security, isin or cusip. 
    Each ticker entry provides a description, matching symbol, and asset type.""",
    parameters={
        "type": "object",
        "properties": {
            "q": {
                "type": "string",
                "description": """The symbol or ticker to search for."""
            },
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is 'US' for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            },
            "company": {
                "type": "string",
                "description": "The company you're searching for."
            }
        },
        "required": ["q", "exchange", "query", "company"]
    }
)

decl_get_symbol_quote_1 = types.FunctionDeclaration(
    name="get_symbol_quote_1",
    description="""Search for the current price or quote of a stock ticker or symbol. The response is
                   provided in json format. Each response contains the following key-value pairs:
                   
                   c: Current price,
                   d: Change,
                  dp: Percent change,
                   h: High price of the day,
                   l: Low price of the day,
                   o: Open price of the day,
                  pc: Previous close price,
                   t: Epoch timestamp of price in seconds.

                   Parse the response and respond according to this information.""",
    parameters={
        "type": "object",
        "properties": {
            "symbol": {
                "type": "string",
                "description": "The stock ticker symbol for a company, security, isin, or cusip." 
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            },
            "exchange": {
                "type": "string",
                "description": "The exchange code used to filter quotes. This must always be 'US'."
            }
        },
        "required": ["symbol", "query", "exchange"]
    }
)

decl_get_local_datetime = types.FunctionDeclaration(
    name="get_local_datetime",
    description="""Converts an array of timestamps from epoch time to the local timezone format. The result is an array
                   of date and time in locale appropriate format. Suitable for use in a locale appropriate response.
                   Treat this function as a vector function. Always prefer to batch timestamps for conversion. Use this
                   function to format date and time in your responses.""",
    parameters={
        "type": "object",
        "properties": {
            "t": {
                "type": "array",
                "description": """An array of timestamps in seconds since epoch to be converted. The order of
                                  timestamps matches the order of conversion.""",
                "items": {
                    "type": "integer"
                }
            }
        },
        "required": ["t"]
    }
)

decl_get_market_status_1 = types.FunctionDeclaration(
    name="get_market_status_1",
    description="""Get the current market status of global exchanges. Includes whether exchanges are open or closed.  
                   Also includes holiday details if applicable. The response is provided in json format. Each response 
                   contains the following key-value pairs:

                   exchange: Exchange code,
                   timezone: Timezone of the exchange,
                    holiday: Holiday event name, or null if it's not a holiday,
                     isOpen: Whether the market is open at the moment,
                          t: Epoch timestamp of status in seconds (Eastern Time),
                    session: The market session can be 1 of the following values: 
                    
                    pre-market,regular,post-market when open, or null if closed.
                    
                    Parse the response and respond according to this information.""",
    parameters={
        "type": "object",
        "properties": {
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is 'US' for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for."""
            }
        },
        "required": ["exchange"]
    }
)

decl_get_market_session_1 = types.FunctionDeclaration(
    name="get_market_session_1",
    description="Get the current market session of global exchanges.",
    parameters={
        "type": "object",
        "properties": {
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is 'US' for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for."""
            }
        },
        "required": ["exchange"]
    }
)

decl_get_company_peers_1 = types.FunctionDeclaration(
    name="get_company_peers_1",
    description="""Search for a company's peers. Returns a list of peers operating in the same country and in the same
                   sector, industry, or subIndustry. Each response contains the following key-value pairs: 
                   
                   symbol: The company's stock ticker symbol, 
                   peers: A list containing the peers.
                   
                   Each peers entry contains the following key-value pairs:
                   
                   symbol: The peer company's stock ticker symbol, 
                   name: The peer company's name.
                   
                   Parse the response and respond according to this information.""",
    parameters={
        "type": "object",
        "properties": {
            "symbol": {
                "type": "string",
                "description": "The stock ticker symbol of a company to obtain peers."
            },
            "grouping": {
                "type": "string",
                "description": """This parameter may be one of the following values: sector, industry, subIndustry.
                                  Always use subIndustry unless told otherwise."""
            },
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is 'US' for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["symbol", "grouping", "exchange", "query"]
    }
)

decl_get_exchange_codes_1 = types.FunctionDeclaration(
    name="get_exchange_codes_1",
    description="""Get a dictionary mapping all supported exchange codes to their names."""
)

decl_get_exchange_code_1 = types.FunctionDeclaration(
    name="get_exchange_code_1",
    description="""Search for the exchange code to use when filtering by exchange. The result will be one or
                   more exchange codes provided as a comma-separated string value.""",
    parameters={
        "type": "object",
        "properties": {
            "q": {
                "type": "string",
                "description": "Specifies which exchange code to search for."
            }
        },
        "required": ["q"]
    }
)

decl_get_financials_1 = types.FunctionDeclaration(
    name="get_financials_1",
    description="""Get company basic financials such as margin, P/E ratio, 52-week high/low, etc. Parse the response for 
                   key-value pairs in json format and interpret their meaning as stock market financial indicators.""",
    parameters={
        "type": "object",
        "properties": {
            "symbol": {
                "type": "string",
                "description": "Stock ticker symbol for a company."
            },
            "metric": {
                "type": "string",
                "description": "It must always be declared as the value 'all'"
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["symbol", "metric", "query"]
    }
)

decl_get_daily_candlestick_2 = types.FunctionDeclaration(
    name="get_daily_candlestick_2",
    description="""Get a historical daily stock ticker candlestick / aggregate bar (OHLC). 
                   Includes historical daily open, high, low, and close prices. Also includes historical daily trade
                   volume and pre-market/after-hours trade prices. It provides the last trading days' data after 
                   11:59PM Eastern Time.""",
    parameters={
        "type": "object",
        "properties": {
            "stocksTicker": {
                "type": "string",
                "description": "The stock ticker symbol of a company to search for.",
            },
            "date": {
                "type": "string",
                "format": "date-time",
                "description": """The date of the requested candlestick in format YYYY-MM-DD."""
            },
            "adjusted": {
                "type": "string",
                "description": """May be true or false. Indicates if the results should be adjusted for splits.
                                  Use true unless told otherwise."""
            },
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is 'US' for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["stocksTicker", "date", "adjusted", "exchange", "query"]
    },
)

decl_get_company_news_1 = types.FunctionDeclaration(
    name="get_company_news_1",
    description="Retrieve the most recent news articles related to a specified ticker.",
    parameters={
        "type": "object",
        "properties": {
            "symbol": {
                "type": "string",
                "description": "Stock ticker symbol for a company.",
            },
            "from": {
                "type": "string",
                "format": "date-time",
                "description": """A date in format YYYY-MM-DD. It must be older than the parameter 'to'."""
            },
            "to": {
                "type": "string",
                "format": "date-time",
                "description": """A date in format YYYY-MM-DD. It must be more recent than the parameter 'from'. The
                                  default value is today's date."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["symbol", "from", "to", "query"]
    },
)

decl_get_custom_candlestick_2 = types.FunctionDeclaration(
    name="get_custom_candlestick_2",
    description="""Get a historical stock ticker candlestick / aggregate bar (OHLC) over a custom date range and 
                   time interval in Eastern Time. Includes historical open, high, low, and close prices. Also 
                   includes historical daily trade volume and pre-market/after-hours trade prices. It includes 
                   the last trading days' data after 11:59PM Eastern Time.""",
    parameters={
        "type": "object",
        "properties": {
            "stocksTicker": {
                "type": "string",
                "description": "The stock ticker symbol of a company to search for.",
            },
            "multiplier": {
                "type": "integer",
                "description": "This must be included and equal to 1 unless told otherwise."
            },
            "timespan": {
                "type": "string",
                "description": """The size of the candlestick's time window. This is allowed to be one of the following:
                                  second, minute, hour, day, week, month, quarter, or year. The default value is day."""
            },
            "from": {
                "type": "string",
                "format": "date-time",
                "description": """A date in format YYYY-MM-DD must be older than the parameter 'to'."""
            },
            "to": {
                "type": "string",
                "format": "date-time",
                "description": """A date in format YYYY-MM-DD must be more recent than the parameter 'from'. The 
                                  default is one weekday before get_last_market_close.
                                  Replace more recent dates with the default."""
            },
            "adjusted": {
                "type": "string",
                "description": """May be true or false. Indicates if the results should be adjusted for splits.
                                  Use true unless told otherwise."""
            },
            "sort": {
                "type": "string",
                "description": """This must be included. May be one of asc or desc. asc will sort by timestmap in 
                                  ascending order. desc will sort by timestamp in descending order."""
            },
            "limit": {
                "type": "integer",
                "description": """Set the number of base aggregates used to create this candlestick. This must be 5000 
                                  unless told to limit base aggregates to something else."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["stocksTicker", "multiplier", "timespan", "from", "to", "adjusted", "sort", "limit", "query"]
    },
)

decl_get_last_market_close = types.FunctionDeclaration(
    name="get_last_market_close",
    description="""Get the last market close of the specified exchange in Eastern Time. The response has already
                   been converted by get_local_datetime so this step should be skipped.""",
    parameters={
        "type": "object",
        "properties": {
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is 'US' for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for."""
            }
        },
        "required": ["exchange"]
    }
)

decl_get_ticker_overview_2 = types.FunctionDeclaration(
    name="get_ticker_overview_2",
    description="""Retrieve comprehensive details for a single ticker symbol. It's a deep look into a company’s 
    fundamental attributes, including its primary exchange, standardized identifiers (CIK, composite FIGI, 
    share class FIGI), market capitalization, industry classification, and key dates. Also includes branding assets in
    the form of icons and logos.
    """,
    parameters={
        "type": "object",
        "properties": {
            "ticker": {
                "type": "string",
                "description": "Stock ticker symbol of a company."
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["ticker", "query"]
    }
)

decl_get_recommendation_trends_1 = types.FunctionDeclaration(
    name="get_recommendation_trends_1",
    description="""Get the latest analyst recommendation trends for a company.
                The data includes the latest recommendations as well as historical
                recommendation data for each month. The data is classified according
                to these categories: strongBuy, buy, hold, sell, and strongSell.
                The date of a recommendation indicated by the value of 'period'.""",
    parameters={
        "type": "object",
        "properties": {
            "symbol": {
                "type": "string",
                "description": "Stock ticker symbol for a company."
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["symbol", "query"]
    }
)

decl_get_news_with_sentiment_2 = types.FunctionDeclaration(
    name="get_news_with_sentiment_2",
    description="""Retrieve the most recent news articles related to a specified ticker. Each article includes 
                   comprehensive coverage. Including a summary, publisher information, article metadata, 
                   and sentiment analysis.""",
    parameters={
        "type": "object",
        "properties": {
            "ticker": {
                "type": "string",
                "description": "Stock ticker symbol for a company."
            },
            "published_utc.gte": {
                "type": "string",
                "format": "date-time",
                "description": """A date in format YYYY-MM-DD must be older than the parameter 'published_utc.lte'. 
                                  The default value is one-month ago from today's date."""
            },
            "published_utc.lte": {
                "type": "string",
                "format": "date-time",
                "description": """A date in format YYYY-MM-DD must be more recent than the parameter 'published_utc.gte'.
                                  The default is one weekday prior to get_last_market_close (excluding weekends).
                                  Replace more recent dates with the default."""
            },
            "order": {
                "type": "string",
                "description": """Must be desc for descending order, or asc for ascending order.
                                  When order is not specified the default is descending order.
                                  Ordering will be based on the parameter 'sort'."""
            },
            "limit": {
                "type": "integer",
                "description": """This must be included and equal to 1000 unless told otherwise."""
            },
            "sort": {
                "type": "string",
                "description": """The sort field used for ordering. This value must
                                  always be published_utc."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["limit", "ticker", "published_utc.gte", "published_utc.lte", "order", "sort", "query"]
    }
)

decl_get_rag_tool_response = types.FunctionDeclaration(
    name="get_rag_tool_response",
    description="""A database containing useful financial information. Always check here for answers first.""",
    parameters={
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "A question needing an answer. Asked as a simple string."
            }
        }
    }
)

decl_get_wiki_tool_response = types.FunctionDeclaration(
    name="get_wiki_tool_response",
    description="""Answers questions that still have unknown answers. Retrieve a wiki page related to a company, 
                   product, or service. Each web page includes detailed company information, financial indicators, 
                   tickers, symbols, history, and products and services.""",
    parameters={
        "type": "object",
        "properties": {
            "id": {
                "type": "string",
                "description": "The question's company or product. Just the name and no other details."
            },
            "q": {
                "type": "string",
                "description": "The complete, unaltered, query string."
            }
        },
        "required": ["id", "q"]
    }
)

decl_get_search_tool_response = types.FunctionDeclaration(
    name="get_search_tool_response",
    description="Answers questions that still have unknown answers. Use it after checking all your other tools.",
    parameters={
        "type": "object",
        "properties": {
            "q": {
                "type": "string",
                "description": "The question needing an answer. Asked as a simple string."
            },
            "id": {
                "type": "string",
                "description": "The question's company or product. In one word. Just the name and no other details."
            }
        },
        "required": ["q", "id"]
    }
)
```


```python
# Define the system prompt.

instruction = f"""You are a helpful and informative bot that answers finance and stock market questions. 
Only answer the question asked and do not change topic. While the answer is still
unknown you must follow these rules for predicting function call order:

RULE#1: Always consult your other functions before get_search_tool_response.
RULE#2: Always consult get_wiki_tool_response before get_search_tool_response.
RULE#3: Always consult get_search_tool_response last.
RULE#4: Always convert timestamps with get_local_datetime and use the converted date/time in your response.
RULE#5: Always incorporate as much useful information from tools and functions in your response."""
```


```python
# Import the finance api secret keys.

POLYGON_API_KEY = UserSecretsClient().get_secret("POLYGON_API_KEY")
FINNHUB_API_KEY = UserSecretsClient().get_secret("FINNHUB_API_KEY")
```


```python
# Instantiate tools and load the exchange data from source csv.
# - Identifies exchanges by a 1-2 letter code which can be used to filter response data.
# - Also maps the exchange code to exchange details.
try:
    df = pandas.read_csv("/kaggle/input/exchanges/exchanges_src.csv")
except FileNotFoundError as e:
    df = pandas.read_csv("exchanges_src.csv") # local run
df = df.drop(["close_date"], axis=1).fillna("")
df.to_csv("exchanges.csv", index=False)
exchanges = CSVLoader(file_path="exchanges.csv", encoding="utf-8", csv_args={"delimiter": ","}).load()

# Prepare a RAG tool for use and add the exchange data.
tool_rag = RetrievalAugmentedGenerator(api.client, "finance")
tool_rag.add_documents_list(exchanges)

# Prepare a the grounding tools for use.
tool_wiki = WikiGroundingGenerator(api.client, tool_rag)
tool_ground = SearchGroundingGenerator(api.client, tool_rag)
tool_rest = RestGroundingGenerator(tool_rag, with_limits=True)
```

    Generate US->MarketEvent.LAST_CLOSE:   0%|          | 0/1 [00:00<?, ?it/s]


    api.generation_fail.next_model: model is now  gemini-2.0-flash-exp


    Generate US->MarketEvent.LAST_CLOSE:   0%|          | 0/1 [00:00<?, ?it/s]


    api.generation_fail.next_model: model is now  gemini-2.5-flash-preview-09-2025


    Generate US->MarketEvent.LAST_CLOSE:   0%|          | 0/1 [00:03<?, ?it/s]


    api.generation_fail.next_model: model is now  gemini-2.5-flash


    Generate US->MarketEvent.LAST_CLOSE:   0%|          | 0/1 [00:03<?, ?it/s]


    api.generation_fail.next_model: model is now  gemini-2.5-flash-lite-preview-09-2025


    Generate US->MarketEvent.LAST_CLOSE:   0%|          | 0/1 [00:00<?, ?it/s]


    api.generation_fail.next_model: model is now  gemini-2.5-flash-lite


    Generate US->MarketEvent.LAST_CLOSE: 100%|██████████| 1/1 [00:00<00:00,  1.62it/s]
    Generate US->MarketEvent.PRE_OPEN: 100%|██████████| 1/1 [00:00<00:00,  1.37it/s]
    Generate US->MarketEvent.REG_OPEN: 100%|██████████| 1/1 [00:00<00:00,  1.37it/s]
    Generate US->MarketEvent.REG_CLOSE: 100%|██████████| 1/1 [00:00<00:00,  1.69it/s]
    Generate US->MarketEvent.POST_CLOSE: 100%|██████████| 1/1 [00:00<00:00,  1.52it/s]
    Generate document embedding: 0it [00:00, ?it/s]


## Function Calling Expert


```python
# Implement the callable functions and function handler.

def ask_rag_tool(content):
    return tool_rag.generate_answer(content["question"]).text

def ask_wiki_tool(content):
    return tool_wiki.generate_answer(content["q"], content["id"])

def ask_search_tool(content):
    return tool_ground.generate_answer(content["q"], content["id"])

def get_exchange_codes_1(content):
    return tool_rag.get_exchange_codes()

def get_exchange_code_1(content):
    return tool_rag.get_exchange_codes(with_query=content)
    
def last_market_close(content):
    return tool_rag.last_market_close(content["exchange"])
    
def get_symbol_1(content, by_name: bool = True):
    stored = tool_rag.get_api_documents(content["query"], content["q"], "get_symbol_1")
    if len(stored) == 0:
        return tool_rest.get_symbol(content, by_name)
    return json.loads(stored[0].docs)

def get_symbols_1(content):
    return None # todo

def get_name_1(content):
    return get_symbol_1(content, by_name = False)

def get_quote_1(content):
    stored = tool_rag.get_api_documents(content["query"], content["symbol"], "get_quote_1")
    if tool_rag.generated_events(content["exchange"]).is_open():
        return get_current_price_1(content)
    elif len(stored) > 0:
        last_close = parse(tool_rag.last_market_close(content["exchange"])).timestamp()
        for quote in stored:
            if quote.meta["timestamp"] >= last_close:
                return [quote.docs for quote in stored]
    return get_current_price_1(content)

def get_current_price_1(content):
    return tool_rest.get_current_price(content)

def get_market_status_1(content):
    stored, has_update = tool_rag.get_market_status(content['exchange'])
    if has_update:
        with_id = stored[0].store_id if len(stored) > 0 else None
        return tool_rest.get_market_status(content, with_id)
    return stored[0].docs

def get_session_1(content):
    return json.loads(get_market_status_1(content))["session"]

def get_peers_1(content):
    stored = tool_rag.get_peers_document(content["query"], content["symbol"], content['grouping'])
    if len(stored) == 0:
        peers = tool_rest.get_peers(content)
        if peers.count > 0:
            names = []
            for peer in peers.get():
                if peer == content["symbol"]:
                    continue # skip including the query symbol in peers
                name = get_name_1(dict(q=peer, exchange=content["exchange"], query=content["query"]))
                if name != StopGeneration().result:
                    data = {"symbol": peer, "name": name}
                    names.append(data)
            tool_rag.add_peers_document(content["query"], names, content["symbol"], "get_peers_1", content['grouping'])
            return names
        return StopGeneration().result
    return json.loads(stored[0].docs)["peers"]

def local_datetime(content):
    local_t = []
    for timestamp in content["t"]:
        local_t.append(local_date_from_epoch(timestamp))
    return local_t

def local_date_from_epoch(timestamp):
    if len(str(timestamp)) == 13:
        return datetime.fromtimestamp(timestamp/1000, tz=GeneratedEvent.tz()).strftime('%c')
    else:
        return datetime.fromtimestamp(timestamp, tz=GeneratedEvent.tz()).strftime('%c')

def get_financials_1(content):
    stored = tool_rag.get_basic_financials(content["query"], content["symbol"], "get_financials_1")
    if len(stored) == 0:
        return tool_rest.get_basic_financials(content)
    return [chunk.docs for chunk in stored]

def get_news_1(content):
    stored = tool_rag.get_api_documents(content["query"], content["symbol"], "get_news_1")
    if len(stored) == 0:
        return tool_rest.get_news_simple(content)
    return [NewsTypeFinn.model_validate_json(news.docs).summary().model_dump_json() for news in stored]

def get_daily_candle_2(content):
    stored = tool_rag.get_api_documents(
        query=content["query"], topic=content["stocksTicker"], source="daily_candle_2", 
        meta_opt=[{"from_date": content["date"], "adjusted": content["adjusted"]}])
    if len(stored) == 0:
        candle = tool_rest.get_daily_candle(content)
        # Attempt to recover from choosing a holiday.
        candle_date = parse(content["date"])
        if candle.status is RestStatus.NONE and candle_date.weekday() == 0 or candle_date.weekday() == 4:
            if candle_date.weekday() == 0: # index 0 is monday, index 4 is friday
                content["date"] = candle_date.replace(day=candle_date.day-3).strftime("%Y-%m-%d")
            else:
                content["date"] = candle_date.replace(day=candle_date.day-1).strftime("%Y-%m-%d")
            return get_daily_candle_2(content)
        return candle.model_dump_json()
    return [json.loads(candle.docs) for candle in stored]

def get_custom_candle_2(content):
    stored = tool_rag.get_api_documents(
        query=content["query"], topic=content["stocksTicker"], source="custom_candle_2", 
        meta_opt=[{
            "timespan": content["timespan"],
            "adjusted": content["adjusted"],
            "from": content["from"],
            "to": content["to"]}])
    if len(stored) == 0:
        return tool_rest.get_custom_candle(content)
    return [json.loads(candle.docs) for candle in stored]

def get_overview_2(content):
    stored = tool_rag.get_api_documents(content["query"], content["ticker"], "ticker_overview_2")
    if len(stored) == 0:
        return tool_rest.get_overview(content)
    return json.loads(stored[0].docs)

def get_trends_1(content):
    stored = tool_rag.get_api_documents(content["query"], content["symbol"], "trends_1")
    if len(stored) == 0:
        return tool_rest.get_trends_simple(content)
    return [json.loads(trend.docs) for trend in stored]

def get_news_2(content):
    timestamp_from = parse(content["published_utc.gte"]).timestamp()
    timestamp_to = parse(content["published_utc.lte"]).timestamp()
    news_from = tool_rag.get_api_documents(
        content["query"], content["ticker"], "get_news_2", [{"published_utc": timestamp_from}])
    news_to = tool_rag.get_api_documents(
        content["query"], content["ticker"], "get_news_2", [{"published_utc": timestamp_to}])
    if len(news_from) > 0 and len(news_to) > 0:
        stored = tool_rag.get_api_documents(
            content["query"], content["ticker"], "get_news_2",
            [{"published_utc": {"$gte": timestamp_from}},
             {"published_utc": {"$lte": timestamp_to}}])
        return [NewsTypePoly.model_validate_json(news.docs).summary().model_dump_json() for news in stored]
    return tool_rest.get_news_tagged(content)
        
finance_tool = types.Tool(
    function_declarations=[
        decl_get_symbol_1,
        decl_get_symbols_1,
        decl_get_name_1,
        decl_get_symbol_quote_1,
        decl_get_market_status_1,
        decl_get_market_session_1,
        decl_get_company_peers_1,
        decl_get_local_datetime,
        decl_get_last_market_close,
        decl_get_exchange_codes_1,
        decl_get_exchange_code_1,
        decl_get_financials_1,
        decl_get_daily_candlestick_2,
        decl_get_custom_candlestick_2,
        decl_get_ticker_overview_2,
        decl_get_recommendation_trends_1,
        decl_get_news_with_sentiment_2,
        decl_get_rag_tool_response,
        decl_get_wiki_tool_response,
        decl_get_search_tool_response
    ]
)

function_handler = {
    "get_symbol_1": get_symbol_1,
    "get_symbols_1": get_symbols_1,
    "get_name_1": get_name_1,
    "get_symbol_quote_1": get_quote_1,
    "get_market_status_1": get_market_status_1,
    "get_market_session_1": get_session_1,
    "get_company_peers_1": get_peers_1,
    "get_local_datetime": local_datetime,
    "get_last_market_close": last_market_close,
    "get_exchange_codes_1": get_exchange_codes_1,
    "get_exchange_code_1": get_exchange_code_1,
    "get_financials_1": get_financials_1,
    "get_daily_candlestick_2": get_daily_candle_2,
    "get_custom_candlestick_2": get_custom_candle_2,
    "get_ticker_overview_2": get_overview_2,
    "get_recommendation_trends_1": get_trends_1,
    "get_news_with_sentiment_2": get_news_2,
    "get_rag_tool_response": ask_rag_tool,
    "get_wiki_tool_response": ask_wiki_tool,
    "get_search_tool_response": ask_search_tool
}
```


```python
# Implement the function calling expert.

@retry.Retry(
    predicate=is_retriable,
    initial=2.0,
    maximum=64.0,
    multiplier=2.0,
    timeout=600,
)
def send_message(prompt):
    #display(Markdown("#### Prompt"))
    #print(prompt, "\n")
    memory.set_prompt(prompt)
    # Enable system prompt, function calling and minimum-randomness.
    config_fncall = types.GenerateContentConfig(
        system_instruction=instruction,
        tools=[finance_tool],
        temperature=0.0
    )
    # Handle cases with multiple chained function calls.
    function_calling_in_process = True
    # Send the initial user prompt and function declarations.
    response = api.retriable(api.client.models.generate_content,
                             model=api(Gemini.Model.GEN),
                             config=config_fncall,
                             contents=memory.contents)
    while function_calling_in_process:
        # A part can be a function call or natural language response.
        for part in response.candidates[0].content.parts:
            if function_call := part.function_call:
                # Extract the function call.
                fn_name = function_call.name
                #display(Markdown("#### Predicted function name"))
                #print(fn_name, "\n")
                # Extract the function call arguments.
                fn_args = {key: value for key, value in function_call.args.items()}
                #display(Markdown("#### Predicted function arguments"))
                #print(fn_args, "\n")
                # Call the predicted function.
                try:
                    api_response = function_handler[fn_name](fn_args)[:20000] # Stay within the input token limit
                except KeyError as e: # Gemini sometimes omits required fn_args
                    api.generation_fail()
                    time.sleep(api.dt_between)
                    send_message(prompt)
                #display(Markdown("#### API response"))
                #print(api_response[:500], "...", "\n")
                # Create an API response part.
                api_response_part = types.Part.from_function_response(
                    name=fn_name,
                    response={"content": api_response},
                )
                memory.update_contents(function_call, api_response_part)
                # Send the updated prompt.
                response = api.retriable(api.client.models.generate_content,
                                         model=api(Gemini.Model.GEN),
                                         config=config_fncall,
                                         contents=memory.contents)
            else:
                # Response may be a summary or reasoning step.
                if len(response.candidates[0].content.parts) == 1:
                    function_calling_in_process = False
                    memory.set_summary(response.text.replace("$", "\\$"))
                    break # No more parts in response.
                else:
                    #display(Markdown("#### Natural language reasoning step"))
                    #print(response)
                    memory.set_reason(response.candidates[0].content.parts[0].text)
                    continue # Next part contains a function call.
        if not function_calling_in_process:
            break # The function calling chain is complete.
            
    # Show the final natural language summary.
    display(Markdown("#### Natural language response"))
    display(Markdown(memory.summary))
```

# RAG Baseline Check


```python
response = tool_rag.get_exchanges_csv(
    """Give me a dictionary in string form. It must contain key:value pairs mapping 
    exchange code to name. Just the dictionary string in pretty form.""")
print(response.candidates[0].content.parts[-1].text)

response = tool_rag.get_exchanges_csv(
    """What is the Germany exchange code? Return only the exchange codes as a simple 
    comma separated value that I can copy.""")
print(response.candidates[0].content.parts[-1].text, "\n")

response = tool_rag.get_exchanges_csv("What are the Germany exchanges and thier corresponding exchange codes?")
print(response.text, "\n")

response = tool_rag.generate_answer("What are Google's stock ticker symbols?")
print(response.text, "\n")

response = tool_rag.generate_answer("What is Facebook's stock ticker symbol?")
print(response.text, "\n")

response = tool_rag.get_exchanges_csv("What are the US exchange operating hours?")
print(response.text, "\n")

response = tool_rag.get_exchanges_csv(
    f"""Answer based on your knowledge of exchange operating hours.
    Do not answer in full sentences. Omit all chat and provide the answer only.
    The fields pre_market and post_market both represent extended operating hours.

    The current date and time: {datetime.now(GeneratedEvent.tz()).strftime('%c')}

    Weekdays are: Mon, Tue, Wed, Thu, Fri.
    On weekdays all exchanges open after pre-market and regular hours.
    On weekdays all exchanges close after regular and post-market hours.
    
    Weekends are: Sat, Sun.
    Always exclude weekends from exchange operating hours.
    A list of holidays in date format mm-dd-yyyy: {tool_rag.holidays["US"]}
    Always exclude holidays from exchange operating hours.
    When the answer is a holiday use the prior weekday for close.
    When the answer is a holiday use the next weekday for open.
    
    Consider the US exchange's operating hours.
    Provide the most recent weekday's close including post_market hours.
    
    Answer with a date that uses this format: '%a %b %d %X %Y'.""")
print(response.candidates[0].content.parts[-1].text)
```

    ```json
    {
      "VN": "Vietnam",
      "AD": "ABU DHABI SECURITIES EXCHANGE",
      "US": "US exchanges (NYSE, Nasdaq)",
      "CO": "OMX NORDIC EXCHANGE COPENHAGEN A/S",
      "QA": "QATAR EXCHANGE",
      "BA": "BOLSA DE COMERCIO DE BUENOS AIRES",
      "MX": "BOLSA MEXICANA DE VALORES (MEXICAN STOCK EXCHANGE)",
      "PR": "PRAGUE STOCK EXCHANGE",
      "HK": "HONG KONG EXCHANGES AND CLEARING LTD",
      "CA": "Egyptian Stock Exchange",
      "AX": "ASX - ALL MARKETS",
      "SX": "DEUTSCHE BOERSE Stoxx",
      "KQ": "KOREA EXCHANGE (KOSDAQ)",
      "DB": "DUBAI FINANCIAL MARKET",
      "PM": "Philippine Stock Exchange",
      "KS": "KOREA EXCHANGE (STOCK MARKET)",
      "ST": "NASDAQ OMX NORDIC STOCKHOLM",
      "DU": "BOERSE DUESSELDORF",
      "TL": "NASDAQ OMX TALLINN",
      "AT": "ATHENS EXCHANGE S.A. CASH MARKET",
      "SW": "SWISS EXCHANGE",
      "LS": "NYSE EURONEXT - EURONEXT LISBON",
      "SI": "SINGAPORE EXCHANGE",
      "RG": "NASDAQ OMX RIGA",
      "CR": "CARACAS STOCK EXCHANGE",
      "SA": "Brazil Bolsa - Sao Paolo",
      "BH": "BAHRAIN BOURSE",
      "NZ": "NEW ZEALAND EXCHANGE LTD",
      "L": "LONDON STOCK EXCHANGE",
      "SZ": "SHENZHEN STOCK EXCHANGE",
      "IC": "NASDAQ OMX ICELAND",
      "KW": "Kuwait Stock Exchange",
      "JK": "INDONESIA STOCK EXCHANGE",
      "BE": "BOERSE BERLIN",
      "TA": "TEL AVIV STOCK EXCHANGE",
      "PA": "NYSE EURONEXT - MARCHE LIBRE PARIS",
      "V": "TSX VENTURE EXCHANGE - NEX",
      "SN": "SANTIAGO STOCK EXCHANGE",
      "BD": "BUDAPEST STOCK EXCHANGE",
      "KL": "BURSA MALAYSIA",
      "CN": "CANADIAN NATIONAL STOCK EXCHANGE",
      "VS": "NASDAQ OMX VILNIUS",
      "ME": "MOSCOW EXCHANGE",
      "CS": "CASABLANCA STOCK EXCHANGE",
      "NL": "Nigerian Stock Exchange",
      "BR": "NYSE EURONEXT - EURONEXT BRUSSELS",
      "NS": "NATIONAL STOCK EXCHANGE OF INDIA",
      "DE": "XETRA",
      "WA": "WARSAW STOCK EXCHANGE/EQUITIES/MAIN MARKET",
      "AS": "NYSE EURONEXT - EURONEXT AMSTERDAM",
      "TG": "DEUTSCHE BOERSE TradeGate",
      "IR": "IRISH STOCK EXCHANGE - ALL MARKET",
      "OL": "OSLO BORS ASA",
      "BO": "BSE LTD",
      "MT": "MALTA STOCK EXCHANGE",
      "BC": "BOLSA DE VALORES DE COLOMBIA",
      "F": "DEUTSCHE BOERSE AG",
      "HE": "NASDAQ OMX HELSINKI LTD",
      "MU": "BOERSE MUENCHEN",
      "IS": "BORSA ISTANBUL",
      "SR": "SAUDI STOCK EXCHANGE",
      "NE": "AEQUITAS NEO EXCHANGE",
      "MI": "Italian Stock Exchange",
      "SS": "SHANGHAI STOCK EXCHANGE",
      "MC": "BOLSA DE MADRID",
      "HA": "Hanover Stock Exchange",
      "VI": "Vienna Stock Exchange",
      "TWO": "TPEx",
      "HM": "HANSEATISCHE WERTPAPIERBOERSE HAMBURG",
      "TW": "TAIWAN STOCK EXCHANGE",
      "TO": "TORONTO STOCK EXCHANGE",
      "SC": "BOERSE_FRANKFURT_ZERTIFIKATE",
      "JO": "JOHANNESBURG STOCK EXCHANGE",
      "SG": "BOERSE STUTTGART",
      "RO": "BUCHAREST STOCK EXCHANGE",
      "T": "TOKYO STOCK EXCHANGE-TOKYO PRO MARKET",
      "BK": "STOCK EXCHANGE OF THAILAND"
    }
    ```
    DE, F, TG, SX, BE, DU, HA, HM, MU, SC, SG 
    
    The Germany exchanges and their corresponding codes are: XETRA (DE), DEUTSCHE BOERSE AG (F), Hanover Stock Exchange (HA), DEUTSCHE BOERSE TradeGate (TG), BOERSE BERLIN (BE), BOERSE DUESSELDORF (DU), HANSEATISCHE WERTPAPIERBOERSE HAMBURG (HM), BOERSE MUENCHEN (MU), DEUTSCHE BOERSE Stoxx (SX), BOERSE_FRANKFURT_ZERTIFIKATE (SC), and BOERSE STUTTGART (SG). 
    
    I don't know. 
    
    I don't know. 
    
    US exchanges operate from 09:30 to 16:00. 
    
    Fri Nov 07 20:00:00 2025


# SC1 Baseline Check


```python
# Wait 59s for rate-limits to reset on FREE-tier.
if api.limit is Gemini.Limit.FREE.value:
    print("Gemini API limit is FREE. Waiting 59s...")
    time.sleep(59)
```

    Gemini API limit is FREE. Waiting 59s...



```python
send_message("What is the current session for US exchanges?")
```

    Upsert chunks embedding: 0it [00:00, ?it/s]



#### Natural language response



The current session for US exchanges is closed.




```python
send_message("What is the US market status?")
```


#### Natural language response



The US market is currently closed as of Sat Nov  8 21:17:00 2025.




```python
send_message("When was the last US market close?")
```


#### Natural language response



The last US market close was Fri Nov 07 20:00:00 2025.




```python
send_message("What is Apple's stock ticker?")
```

    Score similarity to query: 100%|██████████| 10/10 [00:01<00:00,  9.60it/s]
    Generate api embedding: 0it [00:00, ?it/s]



#### Natural language response



Apple's stock ticker is AAPL.




```python
send_message("What is the current price of Amazon stock? Display the result as a json object.")
```

    Generate quote embedding: 0it [00:00, ?it/s]



#### Natural language response



```json
{
"c": 244.41,
"d": 1.37,
"dp": 0.5637,
"h": 244.9,
"l": 238.49,
"o": 242.9,
"pc": 243.04,
"t": 1762549200
}
```



```python
send_message("""Show me Apple's basic financials and help me understand key performance metrics. 
How has the stock performed?""")
```

    api.generation_fail.next_model: model is now  gemini-2.0-flash-exp


    Upsert chunks embedding: 0it [00:00, ?it/s]



#### Natural language response



Here's an overview of Apple's financial performance based on the data you requested:

**Key Financial Metrics and Insights:**

*   **Profitability:**
    *   **Net Profit Margin (TTM):** 26.92% - Apple is very profitable, keeping over 26 cents of every dollar in revenue as profit.
    *   **Operating Margin (TTM):** 31.97% - This shows strong operational efficiency.
    *   **Gross Margin (TTM):** 46.91% - Apple maintains a strong gross margin.
*   **Revenue Growth:**
    *   **Revenue Growth (TTM YoY):** 6.43% - Apple is still growing its revenue.
*   **Earnings Per Share (EPS):**
    *   **EPS (TTM):** \\$7.4593 - Indicates the company's profitability on a per-share basis.
    *   **EPS Growth (TTM YoY):** 22.89% - Apple's earnings per share are growing significantly.
*   **Valuation:**
    *   **Price-to-Earnings Ratio (P/E TTM):** 35.4165 - This suggests investors are willing to pay a premium for Apple's earnings.
    *   **Forward P/E:** 32.7219 - Suggests analysts expect continued earnings growth.
    *   **PEG Ratio (TTM):** 1.5799 - A bit high, suggesting the stock price may be growing faster than earnings.
    *   **Price-to-Sales Ratio (P/S TTM):** 9.5324 - Relatively high, reflecting Apple's brand strength and market dominance.
    *   **Price-to-Book Ratio (P/B):** 53.8023 - High, indicating the market values Apple significantly above its book value.
*   **Return on Equity (ROE):**
    *   **ROE (TTM):** 164.05% - Extremely high, indicating Apple is very efficient at generating profits from shareholders' equity.
*   **Debt & Liquidity:**
    *   **Total Debt/Equity (Annual):** 1.338 - Apple uses a moderate amount of debt relative to equity.
    *   **Current Ratio (Annual):** 0.8933 - Apple's current liabilities are slightly more than its current assets.
    *   **Quick Ratio (Annual):** 0.8588 - A bit below 1, suggesting Apple might have some short-term liquidity challenges.
*   **Stock Performance:**
    *   **52-Week Price Return Daily:** 20.5415%
    *   **52 Week High:** 277.32
    *   **52 Week Low:** 169.2101

**Additional Considerations:**

*   **Financial Health:** While profitable, Apple's current and quick ratios suggest monitoring its short-term liquidity.
*   **Growth:** Apple continues to demonstrate revenue and earnings growth, although revenue growth is slowing.
*   **Market Valuation:** Apple's valuation metrics (P/E, P/S, P/B) are high, reflecting its status as a premium brand and market leader.
*   **Shareholder Returns:** Apple provides returns to shareholders through dividends, with a current dividend yield of 0.3887%.





```python
send_message("I need Apple's daily candlestick from 2025-05-05")
```

    Upsert chunks embedding: 0it [00:00, ?it/s]



#### Natural language response



On 2025-05-05, Apple's stock (AAPL) had the following daily candlestick data:
*   Open: 203.1
*   High: 204.1
*   Low: 198.21
*   Close: 198.89
*   Volume: 69018452
*   Pre-Market: 205.0
*   After-Hours: 198.6



```python
send_message("Tell me who are Apple's peers?")
```

    Score similarity to query: 100%|██████████| 5/5 [00:00<00:00, 19.71it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 1/1 [00:00<00:00,  3.95it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 1/1 [00:00<00:00,  3.97it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 5/5 [00:00<00:00, 19.84it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 1/1 [00:00<00:00,  3.65it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 1/1 [00:00<00:00,  3.74it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 1/1 [00:00<00:00,  3.94it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 2/2 [00:00<00:00,  8.05it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 2/2 [00:00<00:00,  7.88it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 1/1 [00:00<00:00,  3.29it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 1/1 [00:00<00:00,  4.05it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Generate peers embedding: 0it [00:00, ?it/s]



#### Natural language response



Apple's peers include: DELL TECHNOLOGIES -C (DELL), WESTERN DIGITAL CORP (WDC), SANDISK CORP (SNDK), HEWLETT PACKARD ENTERPRISE (HPE), PURE STORAGE INC - CLASS A (PSTG), HP INC (HPQ), SUPER MICRO COMPUTER INC (SMCI), NETAPP INC (NTAP), IONQ INC (IONQ), COMPOSECURE INC-A (CMPO), and QUANTUM COMPUTING INC (QUBT).




```python
send_message("Tell me who are Amazon's peers?")
```

    Score similarity to query: 100%|██████████| 1/1 [00:00<00:00,  4.11it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 2/2 [00:00<00:00,  8.19it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 1/1 [00:00<00:00,  3.97it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 5/5 [00:00<00:00, 19.57it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 2/2 [00:00<00:00,  7.98it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 11/11 [00:00<00:00, 44.55it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 1/1 [00:00<00:00,  3.96it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 1/1 [00:00<00:00,  3.75it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 1/1 [00:00<00:00,  4.03it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Score similarity to query: 100%|██████████| 1/1 [00:00<00:00,  3.90it/s]
    Generate api embedding: 0it [00:00, ?it/s]
    Generate peers embedding: 0it [00:00, ?it/s]



#### Natural language response



Amazon's peers include COUPANG INC (CPNG), EBAY INC (EBAY), DILLARDS INC-CL A (DDS), OLLIE'S BARGAIN OUTLET HOLDI (OLLI), ETSY INC (ETSY), MACY'S INC (M), PATTERN GROUP INC-CL A (PTRN), KOHLS CORP (KSS), SAVERS VALUE VILLAGE INC (SVV), and GROUPON INC (GRPN).




```python
send_message("""Locate Apple's stock ticker, then download recommendation trends of all Apple's peers by sub-industry, 
and then finally compare them.""")
```

    api.zero_error: model is now  gemini-2.0-flash


    Upsert chunks embedding: 0it [00:00, ?it/s]
    Upsert chunks embedding: 0it [00:00, ?it/s]
    Upsert chunks embedding: 0it [00:00, ?it/s]
    Upsert chunks embedding: 0it [00:00, ?it/s]
    Upsert chunks embedding: 0it [00:00, ?it/s]
    Upsert chunks embedding: 0it [00:00, ?it/s]
    Upsert chunks embedding: 0it [00:00, ?it/s]
    Upsert chunks embedding: 0it [00:00, ?it/s]
    Upsert chunks embedding: 0it [00:00, ?it/s]
    Upsert chunks embedding: 0it [00:00, ?it/s]
    Upsert chunks embedding: 0it [00:00, ?it/s]


    api.generation_fail.next_model: model is now  gemini-2.0-flash-exp



#### Natural language response



Okay, I have downloaded the recommendation trends for Apple's peers in the sub-industry. Here's a comparison based on the latest data (2025-11-01):

*   **DELL:** Buy: 18, Hold: 6, Sell: 0, Strong Buy: 8, Strong Sell: 0
*   **WDC:** Buy: 19, Hold: 7, Sell: 0, Strong Buy: 6, Strong Sell: 0
*   **SNDK:** Buy: 10, Hold: 8, Sell: 0, Strong Buy: 7, Strong Sell: 0
*   **HPE:** Buy: 8, Hold: 12, Sell: 0, Strong Buy: 6, Strong Sell: 0
*   **PSTG:** Buy: 13, Hold: 7, Sell: 1, Strong Buy: 6, Strong Sell: 0
*   **HPQ:** Buy: 3, Hold: 16, Sell: 1, Strong Buy: 2, Strong Sell: 0
*   **SMCI:** Buy: 10, Hold: 11, Sell: 3, Strong Buy: 2, Strong Sell: 0
*   **NTAP:** Buy: 9, Hold: 15, Sell: 0, Strong Buy: 3, Strong Sell: 0
*   **IONQ:** Buy: 10, Hold: 3, Sell: 0, Strong Buy: 2, Strong Sell: 0
*   **CMPO:** Buy: 8, Hold: 1, Sell: 1, Strong Buy: 2, Strong Sell: 0
*   **QUBT:** Buy: 5, Hold: 2, Sell: 0, Strong Buy: 2, Strong Sell: 0

**Summary:**

*   **Highest Buy Recommendations:** WDC leads with 19 "buy" recommendations.
*   **Highest Strong Buy Recommendations:** DELL leads with 8 "strong buy" recommendations.
*   **Most Hold Recommendations:** HPQ has the most "hold" recommendations at 16.
*   **Sell Recommendations:** SMCI and CMPO have the most "sell" recommendations with 3 and 1 respectively.





```python
send_message("""Tell me Amazon's current share price and provide candlestick data for the past month. 
Sort the data in descending order by date. Format the prices consistently as currency. 
Round prices to two decimal places. 
Present the data with multiple columns for display in markdown. 
Discuss and provide details about any patterns you notice in the price data. 
Correlate recent patterns with news over the same date range.""")
```

    Add chunks embedding: 0it [00:00, ?it/s]
    Upsert chunks embedding: 0it [00:00, ?it/s]



#### Natural language response



Here's Amazon's current share price and candlestick data for the past month, along with a brief analysis:

**Current Share Price:**

*   As of November 7, 2025, at 16:00 Eastern Time, Amazon's current share price is \$244.41.
*   The change today is \$1.37, which represents a 0.56% increase.
*   The high price of the day was \$244.9, and the low was \$238.49.
*   The previous close price was \$243.04.

**Candlestick Data (Last Month):**

I am presenting the candlestick data in descending order by date.

| Date        | Open    | High    | Low     | Close   | Volume    |
| ----------- | ------- | ------- | ------- | ------- | --------- |
| 2025-11-07  | \$242.90 | \$244.90 | \$238.49 | \$244.41 | 46,374,294|
| 2025-11-06  | \$249.16 | \$250.38 | \$242.17 | \$243.04 | 46,004,201|
| 2025-11-05  | \$249.03 | \$251.00 | \$246.16 | \$250.20 | 40,552,285|
| 2025-11-04  | \$250.38 | \$257.01 | \$248.66 | \$249.32 | 51,546,311|
| 2025-11-03  | \$255.36 | \$258.60 | \$252.90 | \$254.00 | 95,997,714|
| 2025-10-31  | \$250.10 | \$250.50 | \$243.98 | \$244.22 | 166,340,683|
| 2025-10-30  | \$227.06 | \$228.44 | \$222.75 | \$222.86 | 102,252,888|
| 2025-10-29  | \$231.67 | \$232.82 | \$227.76 | \$230.30 | 52,035,936|
| 2025-10-28  | \$228.22 | \$231.49 | \$226.21 | \$229.25 | 47,099,924|
| 2025-10-27  | \$227.66 | \$228.40 | \$225.54 | \$226.97 | 38,266,995|
| 2025-10-24  | \$221.97 | \$225.40 | \$221.90 | \$224.21 | 38,684,853|
| 2025-10-23  | \$219.00 | \$221.30 | \$218.18 | \$221.09 | 31,539,699|
| 2025-10-22  | \$219.30 | \$220.01 | \$216.52 | \$217.95 | 44,308,538|
| 2025-10-21  | \$218.43 | \$223.32 | \$217.99 | \$222.03 | 50,494,565|
| 2025-10-20  | \$213.88 | \$216.69 | \$213.59 | \$216.48 | 38,882,819|
| 2025-10-17  | \$214.56 | \$214.80 | \$211.03 | \$213.04 | 45,986,944|
| 2025-10-16  | \$215.67 | \$218.59 | \$212.81 | \$214.47 | 42,414,591|
| 2025-10-15  | \$216.62 | \$217.71 | \$212.66 | \$215.57 | 45,909,469|
| 2025-10-14  | \$215.56 | \$219.32 | \$212.60 | \$216.39 | 45,665,580|
| 2025-10-13  | \$217.70 | \$220.68 | \$217.04 | \$220.07 | 37,809,650|
| 2025-10-10  | \$226.21 | \$228.25 | \$216.00 | \$216.37 | 72,367,511|
| 2025-10-09  | \$224.99 | \$228.21 | \$221.75 | \$227.74 | 46,412,122|
| 2025-10-08  | \$222.92 | \$226.73 | \$221.19 | \$225.22 | 46,685,985|
| 2025-10-07  | \$220.88 | \$222.89 | \$220.17 | \$221.78 | 31,194,678|

**Observations and Recent News Correlation:**

*   **Late October Surge:**  There was a significant surge in price and volume around the end of October. News from that period indicates positive sentiment around Amazon's Q3 earnings, growth in AWS, and strategic AI partnerships, particularly with OpenAI. The \$38 billion OpenAI deal and strong AWS growth appear to be major drivers.
*   **Early November Dip and Recovery:** Early November saw a dip, followed by a partial recovery. News suggests a broader tech stock downturn ("Magnificent Seven Wiped Out") and concerns about AI investment sustainability may have contributed. However, positive news regarding Amazon's continued strength in AWS and AI investments likely supported the recovery.
*   **Volatility:** The candlestick data shows considerable volatility throughout the month. This aligns with news articles discussing market corrections, AI investment uncertainties, and shifting investor sentiment.
*   **AI Focus:**  Throughout the month, news consistently highlights Amazon's focus on AI, both in its AWS cloud services and its internal operations. This is a key theme influencing investor perceptions.
*   **Workforce Reductions:**  It's worth noting that news of planned workforce reductions also surfaced during this period. While this might initially seem negative, some analysts interpreted it as a strategic move to improve efficiency and prepare for an AI-driven future.

**Disclaimer:** I am an AI and cannot provide financial advice. This analysis is for informational purposes only.




```python
send_message("What is Apple's ticker overview")
```

    Upsert chunks embedding: 0it [00:00, ?it/s]



#### Natural language response



Here is an overview of Apple Inc. (AAPL):
*   **Name:** Apple Inc.
*   **Market:** stocks
*   **Locale:** us
*   **Primary Exchange:** XNAS
*   **CIK:** 0000320193
*   **Composite FIGI:** BBG000B9XRY4
*   **Share Class FIGI:** BBG001S5N8V8
*   **Market Capitalization:** \$3,967,007,489,910.0005
*   **Phone Number:** (408) 996-1010
*   **Address:** ONE APPLE PARK WAY, CUPERTINO, CA 95014
*   **Description:** Apple is among the largest companies in the world, with a broad portfolio of hardware and software products targeted at consumers and businesses. Apple's iPhone makes up a majority of the firm sales, and Apple's other products like Mac, iPad, and Watch are designed around the iPhone as the focal point of an expansive software ecosystem. Apple has progressively worked to add new applications, like streaming video, subscription bundles, and augmented reality. The firm designs its own software and semiconductors while working with subcontractors like Foxconn and TSMC to build its products and chips. Slightly less than half of Apple's sales come directly through its flagship stores, with a majority of sales coming indirectly through partnerships and distribution.
*   **SIC Code:** 3571 (ELECTRONIC COMPUTERS)
*   **Homepage URL:** https://www.apple.com
*   **Total Employees:** 166,000
*   **List Date:** 1980-12-12
*   **Branding:**
    *   **Logo URL:** https://api.polygon.io/v1/reference/company-branding/YXBwbGUuY29t/images/2025-04-04_logo.svg
    *   **Icon URL:** https://api.polygon.io/v1/reference/company-branding/YXBwbGUuY29t/images/2025-04-04_icon.png
*   **Share Class Shares Outstanding:** 14,840,390,000
*   **Weighted Shares Outstanding:** 14,776,353,000
*   **Round Lot:** 100




```python
send_message("Tell me about Amazon's historical and current recommendation trends")
```

    Upsert chunks embedding: 0it [00:00, ?it/s]



#### Natural language response



Here are the recommendation trends for Amazon:
In November 2025, there were 22 strong buy, 54 buy, 2 hold, 0 sell, and 0 strong sell recommendations.
In October 2025, there were 23 strong buy, 52 buy, 3 hold, 0 sell, and 0 strong sell recommendations.
In September 2025, there were 23 strong buy, 52 buy, 4 hold, 0 sell, and 0 strong sell recommendations.
In August 2025, there were 24 strong buy, 51 buy, 4 hold, 0 sell, and 0 strong sell recommendations.



```python
send_message("What is Google's stock ticker symbol?")
```

    Score wiki search by similarity to topic: 0it [00:00, ?it/s]


    api.zero_error: model is now  gemini-2.0-flash


    Generate wiki embeddings: 0it [00:00, ?it/s]



#### Natural language response



Google's shares are listed on the NASDAQ stock exchange under the ticker symbols GOOGL and GOOG. It is also listed on the Frankfurt Stock Exchange under the ticker symbol GGQ1. These ticker symbols now refer to Alphabet Inc., Google's holding company.




```python
send_message("What is MGM Studio's stock symbol?")
```

    Score wiki search by similarity to topic: 0it [00:00, ?it/s]
    Generate wiki embeddings: 0it [00:00, ?it/s]



#### Natural language response



I am unable to find the stock symbol for MGM Studios.



```python
send_message("What is MGM Studio's owner company stock symbol?")
```

    Score similarity to query: 100%|██████████| 2/2 [00:00<00:00,  3.82it/s]
    Generate api embedding: 0it [00:00, ?it/s]



#### Natural language response



MGM Studios is owned by Amazon, and its stock symbol is AMZN.




```python
send_message("What is Facebook's stock ticker symbol?")
```

    api.generation_fail.next_model: model is now  gemini-2.0-flash-exp


    Score wiki search by similarity to topic: 0it [00:00, ?it/s]
    Generate wiki embeddings: 0it [00:00, ?it/s]



#### Natural language response



Facebook's stock ticker symbol is META.




```python
send_message("""Compare Amazon's bullish versus bearish predictions from Oct 01 2025 until today. 
Include a discussion of recommendation trends, and sentiment analysis of news from the same dates. 
Discuss any patterns or correlations you find.""")
```

    Add chunks embedding: 0it [00:00, ?it/s]



#### Natural language response



Between October 1, 2025, and November 8, 2025, here's a comparison of bullish versus bearish predictions for Amazon, incorporating recommendation trends and sentiment analysis of news:

**Recommendation Trends:**

Based on analyst recommendation trends, the sentiment leans bullish.
*   August 1, 2025: Buy (51), Hold (4), Sell (0), Strong Buy (24)
*   September 1, 2025: Buy (52), Hold (4), Sell (0), Strong Buy (23)
*   October 1, 2025: Buy (52), Hold (3), Sell (0), Strong Buy (23)
*   November 1, 2025: Buy (54), Hold (2), Sell (0), Strong Buy (22)

The number of "Buy" recommendations increased from August to November, while "Hold" recommendations fluctuated slightly. There were no "Sell" recommendations during this period.

**Sentiment Analysis of News:**

The news articles from October 1, 2025, to November 8, 2025, present a mixed sentiment regarding Amazon:

*   **Positive Sentiments:** Many articles highlight Amazon's growth in AWS, AI innovations, and strategic partnerships, particularly with OpenAI. Several analysts project a potential 50% stock price increase.
*   **Neutral Sentiments:** Some articles present a neutral stance, mentioning Amazon in the context of broader market trends, partnerships, or as a sales platform for various products.
*   **Negative Sentiments:** Some articles point out concerns such as job cuts, high AI infrastructure spending eroding free cash flow, and increased competition in the cloud computing market.

**Patterns and Correlations:**

1.  **AI Focus:** A recurring theme is Amazon's investment and involvement in AI. Positive sentiment often correlates with news of AI partnerships, AWS growth driven by AI, and potential for AI to improve operational efficiency.
2.  **Cloud Computing:** Amazon's AWS continues to be a significant driver of positive sentiment. Accelerating growth in AWS is frequently mentioned as a reason for investor optimism.
3.  **Job Cuts:** The announcement of job cuts is a recurring negative theme, potentially impacting consumer confidence and indicating cost-cutting measures.
4.  **Market Conditions:** Broader market conditions and economic trends also influence sentiment. For example, concerns about a potential AI bubble or market correction can negatively impact sentiment towards Amazon.
5.  **Stock Splits:** Articles discuss potential stock splits, which tend to generate positive sentiment due to increased accessibility for investors.

**Overall:**

While analyst recommendations remain largely bullish, the news sentiment is more nuanced. The positive sentiment is driven by Amazon's strong position in cloud computing and AI, while negative sentiment arises from concerns about cost management, competition, and broader market conditions.




```python
send_message("""Compare Google's bullish versus bearish predictions from Oct 01 2025 until today. 
Include a discussion of recommendation trends, and sentiment analysis of news from the same dates. 
Discuss any patterns or correlations you find.""")
```

    Upsert chunks embedding: 0it [00:00, ?it/s]
    Add chunks embedding: 0it [00:00, ?it/s]


    api.zero_error: model is now  gemini-2.0-flash



#### Natural language response



Between October 1, 2025, and November 8, 2025, here's a comparison of Google's bullish versus bearish predictions:

**Recommendation Trends:**
*   The recommendation trends for Google (GOOGL) show a consistent bullish sentiment from analysts. In October 2025, there were 39 buy, 13 hold, 21 strong buy, and 0 sell recommendations. In November 2025, the numbers shifted slightly to 41 buy, 12 hold, 21 strong buy, and 0 sell recommendations. This indicates a stable and positive outlook from analysts.

**Sentiment Analysis of News:**
*   The news articles from October 1, 2025, to November 8, 2025, show a generally positive sentiment towards Google. Many articles highlight Google's strong position in AI, cloud computing, and digital advertising. There are also mentions of Google's innovative AI technologies, such as the Gemini AI model, and its strategic partnerships with other companies.
*   However, there are also some articles with neutral or negative sentiment. Some articles discuss potential challenges to Google's market dominance from competitors like OpenAI and the impact of broader market trends.

**Patterns and Correlations:**
*   There appears to be a correlation between positive news sentiment and analyst recommendations. The consistently bullish recommendation trends align with the generally positive news coverage of Google's AI initiatives and financial performance.
*   The news articles suggest that Google's success is closely tied to its ability to innovate in AI and maintain its competitive edge in key markets. Any potential challenges or negative news events could impact analyst sentiment and stock performance.

In summary, the overall outlook for Google between October 1, 2025, and November 8, 2025, appears to be positive, with strong analyst recommendations and generally favorable news sentiment. However, it's important to consider potential challenges and monitor market trends to assess the company's long-term prospects.




```python
send_message("""How is the outlook for Apple based on trends and news sentiment from July 01 2025 until today? 
Perform the same analysis on all peers by sub-industry. Then compare Apple result to it's peers.""")
```

    Add chunks embedding: 0it [00:00, ?it/s]
    Add chunks embedding: 0it [00:00, ?it/s]
    Add chunks embedding: 0it [00:00, ?it/s]
    Add chunks embedding: 0it [00:00, ?it/s]


    api.refill_rpm  15


    Add chunks embedding: 0it [00:00, ?it/s]
    Add chunks embedding: 0it [00:00, ?it/s]
    Add chunks embedding: 0it [00:00, ?it/s]
    Add chunks embedding: 0it [00:00, ?it/s]


    limited 4/min, waiting 11.212908029556274s
    api.refill_rpm  15


    Add chunks embedding: 0it [00:00, ?it/s]
    Add chunks embedding: 0it [00:00, ?it/s]



#### Natural language response



Based on the analysis of analyst recommendation trends and news sentiment from July 01 2025 until today (November 8, 2025), here's an outlook for Apple and its peers by sub-industry:

**Apple (AAPL):**

*   **Recommendation Trends:** Analyst recommendations for Apple are consistently positive, with a majority of analysts rating the stock as a "Buy" or "Strong Buy" throughout the period from August to November 2025.
*   **News Sentiment:** News sentiment is mixed. Some articles highlight Apple's strong iPhone 17 sales and potential in AI, while others express concerns about its AI strategy, trade tensions, and high valuation. Warren Buffett has also been reducing his stake in Apple.

**Peers (by Sub-Industry):**

Here's an analysis of Apple's peers in the sub-industry, focusing on recommendation trends and news sentiment:

*   **Dell Technologies (DELL):**
    *   **Recommendation Trends:** Analyst recommendations are mostly positive, with a majority rating the stock as "Buy" or "Strong Buy".
    *   **News Sentiment:** News sentiment is positive, highlighting strong AI server demand, growing backlog, and increased operating profit margins.
*   **Western Digital (WDC):**
    *   **Recommendation Trends:** Analyst recommendations are mostly positive, with a majority rating the stock as "Buy" or "Strong Buy".
    *   **News Sentiment:** News sentiment is positive, driven by expansion in data storage demand and AI infrastructure growth.
*   **Hewlett Packard Enterprise (HPE):**
    *   **Recommendation Trends:** Analyst recommendations are mixed, with a significant number of "Hold" ratings.
    *   **News Sentiment:** News sentiment is mixed, with some articles highlighting strategic collaborations and AI initiatives, while others point to strategic restructuring costs compressing profit margins.
*   **Super Micro Computer (SMCI):**
    *   **Recommendation Trends:** Analyst recommendations are mixed, with a significant number of "Hold" ratings.
    *   **News Sentiment:** News sentiment is mixed, with some articles highlighting strong AI order backlog but declining margins and negative cash flow.
*   **NetApp (NTAP):**
    *   **Recommendation Trends:** Analyst recommendations are mixed, with a significant number of "Hold" ratings.
    *   **News Sentiment:** News sentiment is neutral, with limited news coverage during the specified period.
*   **IonQ (IONQ):**
    *   **Recommendation Trends:** Analyst recommendations are mostly positive, with a majority rating the stock as "Buy" or "Strong Buy".
    *   **News Sentiment:** News sentiment is mixed, with some articles highlighting the company's technological advancements and potential in quantum computing, while others express concerns about its high valuation and lack of commercial viability.
*   **CompoSecure (CMPO):**
    *   **Recommendation Trends:** Analyst recommendations are mostly positive, with a majority rating the stock as "Buy" or "Strong Buy".
    *   **News Sentiment:** News sentiment is positive, highlighting the company's planned business combination with Husky Technologies.
*   **Quantum Computing Inc (QUBT):**
    *   **Recommendation Trends:** Analyst recommendations are mixed, with a significant number of "Hold" ratings.
    *   **News Sentiment:** News sentiment is negative, highlighting the company's declining revenue, rising operating costs, and minimal sales.

**Comparison:**

*   Apple's recommendation trends are generally positive, but its news sentiment is more mixed compared to some of its peers like Dell and Western Digital.
*   Several peers, particularly those involved in AI infrastructure (e.g., Dell, Super Micro Computer), are experiencing strong growth and positive news sentiment.
*   Quantum computing stocks (e.g., IonQ, Quantum Computing Inc.) are highly speculative, with significant potential but also substantial risks.

**Overall:**

The outlook for Apple is cautiously optimistic, with a need to address AI concerns and navigate trade tensions. Some peers in AI infrastructure are showing stronger growth potential, while quantum computing stocks are highly speculative.



    api.refill_rpm  15



```python
api.push_default_model("gemini-2.5-flash")
send_message("""What does the recent news say about Apple and the impact of tariffs? From 2025-09-01 up to today. 
Also locate candlestick data for the same dates. 
Discuss in detail any correlations in patterns between the candlestick and news data. Ignore duplicate news entry.""")
```

    Upsert chunks embedding: 0it [00:00, ?it/s]
    WARNING:google_genai.types:Warning: there are non-text parts in the response: ['thought_signature'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.



#### Natural language response



Here's a detailed look at the recent news regarding Apple and the impact of tariffs, along with candlestick data for the same period (2025-09-01 to 2025-11-08), and an analysis of their correlations:

**Recent News on Apple and Tariffs (2025-09-01 to 2025-11-08):**

The news from this period indicates a mixed but generally cautious sentiment surrounding Apple and the impact of tariffs.

*   **Negative Impacts and Concerns:**
    *   **October 26, 2025:** News highlighted potential significant challenges for Apple due to US-China trade tensions, specifically mentioning rare earth element export restrictions that could disrupt iPhone component supply chains by November 1st.
    *   **October 13, 2025:** Reports indicated that Apple's stock performance was being impacted by escalating trade barriers between the United States and China.
    *   **October 10, 2025:** President Trump's renewed tariff threats against China triggered a significant market selloff, with tech stocks, including Apple, experiencing substantial losses.
    *   **September 4, 2025:** Apple was noted as facing potential tariff threats.
    *   **October 9, 2025:** While not directly about Apple's tariffs, news of Apple losing smartphone market leadership to Huawei in China could be an indirect consequence of trade tensions.
    *   **November 6, 2025:** US stock futures fell after the Supreme Court raised doubts about Trump's tariff authority, creating market uncertainty that could affect Apple.

*   **Mitigation Strategies and Positive Adaptations:**
    *   **October 28, 2025:** Apple was reported to have successfully navigated Trump's tariff policies by making strategic U.S. investments, relocating iPhone production, and securing exemptions from Chinese and Indian tariffs.
    *   **October 31, 2025:** Apple invested \$500 million in MP Materials for rare earth magnet recycling, a proactive step to address supply chain risks stemming from China's export controls on rare earth magnets.
    *   **September 17, 2025:** Apple was noted for its large-scale investments in Vietnam to expand production capacity, a move likely aimed at diversifying its supply chain and mitigating tariff impacts.
    *   **September 4, September 12, October 6, October 16, 2025:** Multiple reports highlighted Apple's involvement in transformative deals with MP Materials to secure a domestic supply of rare earth materials, further demonstrating its efforts to reduce reliance on potentially tariff-affected regions.
    *   **October 6, 2025:** Apple was mentioned as striking side deals to mitigate tariff impacts.
    *   **September 30, 2025:** Apple contributed to chip industry investments, which could be part of a broader strategy to strengthen its domestic supply chain and reduce tariff exposure.

**Candlestick Data for Apple (AAPL) from 2025-09-01 to 2025-11-08:**

Here's a summary of Apple's daily open, high, low, and close prices during the specified period:

| Date         | Open    | High    | Low     | Close   |
| :----------- | :------ | :------ | :------ | :------ |
| Sep 1, 2025  | 229.25  | 230.85  | 226.97  | 229.72  |
| Sep 2, 2025  | 237.21  | 238.85  | 234.36  | 238.47  |
| Sep 3, 2025  | 238.45  | 239.90  | 236.74  | 239.78  |
| Sep 4, 2025  | 240.00  | 241.32  | 238.49  | 239.69  |
| Sep 5, 2025  | 239.30  | 240.15  | 236.34  | 237.88  |
| Sep 8, 2025  | 237.00  | 238.78  | 233.36  | 234.35  |
| Sep 9, 2025  | 232.19  | 232.42  | 225.95  | 226.79  |
| Sep 10, 2025 | 226.88  | 230.45  | 226.65  | 230.03  |
| Sep 11, 2025 | 229.22  | 234.51  | 229.02  | 234.07  |
| Sep 12, 2025 | 237.00  | 238.19  | 235.03  | 236.70  |
| Sep 15, 2025 | 237.18  | 241.22  | 236.32  | 238.15  |
| Sep 16, 2025 | 238.97  | 240.10  | 237.73  | 238.99  |
| Sep 17, 2025 | 239.97  | 241.20  | 236.65  | 237.88  |
| Sep 18, 2025 | 241.23  | 246.30  | 240.21  | 245.50  |
| Sep 19, 2025 | 248.30  | 256.64  | 248.12  | 256.08  |
| Sep 22, 2025 | 255.88  | 257.34  | 253.58  | 254.43  |
| Sep 23, 2025 | 255.22  | 255.74  | 251.04  | 252.31  |
| Sep 24, 2025 | 253.21  | 257.17  | 251.71  | 256.87  |
| Sep 25, 2025 | 254.10  | 257.60  | 253.78  | 255.46  |
| Sep 26, 2025 | 254.56  | 255.00  | 253.01  | 254.43  |
| Sep 29, 2025 | 254.86  | 255.92  | 253.11  | 254.63  |
| Sep 30, 2025 | 255.04  | 258.79  | 254.93  | 255.45  |
| Oct 1, 2025  | 256.58  | 258.18  | 254.15  | 257.13  |
| Oct 2, 2025  | 254.67  | 259.24  | 253.95  | 258.02  |
| Oct 3, 2025  | 257.99  | 259.07  | 255.05  | 256.69  |
| Oct 6, 2025  | 256.81  | 257.40  | 255.43  | 256.48  |
| Oct 7, 2025  | 256.52  | 258.52  | 256.11  | 258.06  |
| Oct 8, 2025  | 257.81  | 258.00  | 253.14  | 254.04  |
| Oct 9, 2025  | 254.94  | 256.38  | 244.00  | 245.27  |
| Oct 10, 2025 | 249.38  | 249.69  | 245.56  | 247.66  |
| Oct 13, 2025 | 246.60  | 248.85  | 244.70  | 247.77  |
| Oct 14, 2025 | 249.49  | 251.82  | 247.47  | 249.34  |
| Oct 15, 2025 | 248.25  | 249.04  | 245.13  | 247.45  |
| Oct 16, 2025 | 248.02  | 253.38  | 247.27  | 252.29  |
| Oct 17, 2025 | 255.89  | 264.38  | 255.63  | 262.24  |
| Oct 20, 2025 | 261.88  | 265.29  | 261.83  | 262.77  |
| Oct 21, 2025 | 262.65  | 262.85  | 255.43  | 258.45  |
| Oct 22, 2025 | 259.94  | 260.62  | 258.01  | 259.58  |
| Oct 23, 2025 | 261.19  | 264.13  | 259.18  | 262.82  |
| Oct 24, 2025 | 264.88  | 269.12  | 264.65  | 268.81  |
| Oct 27, 2025 | 268.99  | 269.89  | 268.15  | 269.00  |
| Oct 28, 2025 | 269.28  | 271.41  | 267.11  | 269.70  |
| Oct 29, 2025 | 271.99  | 274.14  | 268.48  | 271.40  |
| Oct 30, 2025 | 276.99  | 277.32  | 269.16  | 270.37  |
| Oct 31, 2025 | 270.42  | 270.85  | 266.25  | 269.05  |
| Nov 3, 2025  | 268.33  | 271.49  | 267.62  | 270.04  |
| Nov 4, 2025  | 268.61  | 271.70  | 266.93  | 270.14  |
| Nov 5, 2025  | 267.89  | 273.40  | 267.89  | 269.77  |
| Nov 6, 2025  | 269.80  | 272.29  | 266.77  | 268.47  |

**Correlations in Patterns between Candlestick and News Data:**

Several correlations can be observed between the tariff-related news and Apple's stock movements:

*   **Early September Surge (Sep 2-4):** Apple's stock experienced a notable upward trend, with the closing price increasing from \$229.72 to \$239.69. This period coincided with positive news on September 3rd about Alphabet dodging antitrust remedies, which generally boosted tech stocks, and on September 4th, news of Apple's involvement in a transformative deal with MP Materials, signaling proactive steps to mitigate tariff impacts.
*   **Mid-September Drop (Sep 9):** The stock saw a significant drop from \$234.35 to \$226.79. This aligns with news on September 9th highlighting Apple facing challenges with AI features and potential tariffs, contributing to negative sentiment.
*   **Mid-September Rally (Sep 18-19):** Apple's stock showed strong gains, jumping from \$237.88 to \$256.08 over two days. This period followed news on September 17th about Apple investing in Vietnam for production capacity expansion (a tariff mitigation strategy) and positive reports on September 18th about strong early sales for the new iPhone lineup.
*   **Early October Decline (Oct 9-10):** The stock experienced a significant drop from \$254.04 to \$245.27 on October 9th, and continued to decline slightly on October 10th. This downturn aligns with the broader market selloff triggered by President Trump's renewed tariff threats on October 10th. Additionally, news on October 9th about Apple losing smartphone market leadership in China (potentially tariff-related) and general market concerns about tariffs likely contributed to the negative pressure.
*   **Late October Volatility (Oct 26-31):** The stock showed some volatility, with a significant drop after an opening high on October 30th. This period saw news on October 26th about Apple potentially being hit hard by tariffs, which could have contributed to the negative sentiment. However, positive news on October 28th about Apple successfully navigating tariff policies and on October 31st about its investment in rare earth magnets for supply chain security might have helped to temper further declines or set the stage for a rebound.
*   **Early November Slight Dip (Nov 6):** A slight dip in the stock price on November 6th coincided with news that US stock futures fell due to doubts about Trump's tariff authority, indicating ongoing market sensitivity to tariff-related uncertainties.

In conclusion, there is a discernible correlation between news regarding tariffs and Apple's stock performance during this period. Positive news about Apple's strategies to mitigate tariff impacts or broader market optimism tended to coincide with stock price increases, while renewed tariff threats or concerns about their impact often led to declines or increased volatility. However, it's crucial to remember that multiple factors influence stock prices, and these correlations highlight the significant role that tariff-related developments played in shaping investor sentiment for Apple.


    api.refill_rpm  10

