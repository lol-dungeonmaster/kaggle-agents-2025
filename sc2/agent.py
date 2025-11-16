from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.genai import types

root_agent = Agent(
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=types.HttpRetryOptions(
            attempts=10, 
            exp_base=1,
            initial_delay=10,
            http_status_codes=[429, 500, 503, 504],
        )
    ),
    name='sc2_root',
    description='A helpful assistant for finance questions.',
    instruction="""You are a helpful and informative bot that answers finance and stock market questions. 
    Only answer the question asked and do not change topic. Follow these rules at all times:

    RULE#1: Use all your agents and tools to source answers.
    RULE#2: Convert all timestamps to local date/time.
    RULE#3: Incorporate as much useful information in your final response.""",
)
