from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.genai import types
from .finance_tools_decl import *

retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=2,
    initial_delay=3,
    http_status_codes=[429, 500, 503, 504],
)

root_agent = Agent(
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config),
    name="sc2_summary",
    description="A helpful assistant for finance questions.",
    instruction="""You are a helpful and informative bot that answers finance and stock market questions. 
    Only answer the question asked and do not change topic. Follow these rules at all times:

    RULE#1: Use all available resources to source answers.
    RULE#2: Convert all timestamps to local date/time before you respond.
    RULE#3: Incorporate as much useful information in your final response.""",
    output_key="user_interest"
)

planner_agent = Agent(
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=retry_config),
    name="sc2_planner",
    description="A helpful planner of function calls.",
    instruction="""You are a helpful and informative bot that plans function calls. 
    Think step-by-step using your knowledge of available functions. Then provide a detailed plan of function calls.
    Do not call the functions yourself, only provide your final plan.""",
    tools=finance_tools,
    output_key="interest_plan"
)
