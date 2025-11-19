from google.api_core import retry
from google.genai.models import Models
from google.genai import errors
from google.genai import types
from lmnr import Laminar
from .secret import UserSecretsClient

is_retriable = lambda e: (isinstance(e, errors.APIError) and e.code in {429, 503, 500})
Models.generate_content = retry.Retry(predicate=is_retriable)(Models.generate_content)
Models.embed_content = retry.Retry(predicate=is_retriable)(Models.embed_content)

# Activate Laminar auto-instrumentation.
try:
    Laminar.initialize(project_api_key=UserSecretsClient().get_secret("LMNR_PROJECT_API_KEY"))
except:
    print("Skipping Laminar.initialize()")

retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=2,
    initial_delay=3,
    http_status_codes=[429, 500, 503, 504],
)