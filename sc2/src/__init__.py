import inspect, logging, sys
from google.api_core import retry
from google.genai.models import Models
from google.genai import errors
from google.genai import types
from lmnr import Laminar

log = logging.getLogger()

# Tqdm sends output to stderr which doesn't mix well with logger output.
# Define a stderr wrapper to forward output to logger.
class StderrToLog:
    buffer = ""

    def write(self, message: str):
        msg = message.rstrip()
        if msg and msg is not self.buffer: # ignore empty/duplicate writes
            self.buffer = msg
            caller_name = inspect.stack()[1].frame.f_code.co_name
            if caller_name in ["inner","outer"]: # tqdm internals
                log.info(msg)
            else:
                logging.getLogger("stderr").error(msg)
    
    def flush(self):
        pass

sys.stderr = StderrToLog()

is_retriable = lambda e: (isinstance(e, errors.APIError) and e.code in {429, 503, 500})
Models.generate_content = retry.Retry(predicate=is_retriable)(Models.generate_content)
Models.embed_content = retry.Retry(predicate=is_retriable)(Models.embed_content)

retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=2,
    initial_delay=3,
    http_status_codes=[429, 500, 503, 504],
)

from .secret import UserSecretsClient

# Activate Laminar auto-instrumentation.
try:
    Laminar.initialize(project_api_key=UserSecretsClient().get_secret("LMNR_PROJECT_API_KEY"))
except:
    log.info("Skipping Laminar.initialize()")

import os
from .api import Api

try:
    api = Api(with_limit=int(os.environ["API_LIMIT"]), default_model=os.environ["GEN_DEFAULT"])
except KeyError as e:
    log.error("sc2.__init__: incomplete .env (API_LIMIT/GEN_DEFAULT)")
else:
    log.info("sc2.__init__: the api-helper is ready")

from .tool.rest import RestGroundingTool
from .tool.search import SearchGroundingTool
from .tool.wiki import WikiGroundingTool

RGT = RestGroundingTool(api, with_limits=True)
log.info("sc2.__init__: RestGroundingTool is ready")
SGT = SearchGroundingTool(api)
log.info("sc2.__init__: SearchGroundingTool is ready")
WGT = WikiGroundingTool(api)
log.info("sc2.__init__: WikiGrounding is ready")