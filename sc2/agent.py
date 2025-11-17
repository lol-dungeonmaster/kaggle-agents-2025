from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import AgentTool
from google.genai import types
from .finance_tools_decl import *

retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=2,
    initial_delay=3,
    http_status_codes=[429, 500, 503, 504],
)

summary_agent = Agent(
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config),
    name="sc2_summary",
    instruction="""Read the provided function call plan and create a concise summary.
    Follow these rules at all times:

    RULE#1: Convert all timestamps to local date/time before you respond.
    RULE#2: Incorporate as much useful information in your final response.
    
    Function call plan:
    {interest_plan}""",
    tools=[local_datetime],
    output_key="interest_summary",
)

planner_agent = Agent(
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=retry_config),
    name="sc2_planner",
    description="A helpful planner of function calls.",
    instruction="""Based on the question posed provide a step-by-step function call plan to answer it.
    Do NOT call the functions yourself. Only provide your function call instructions.""",
    tools=finance_tools,
    output_key="interest_plan"
)

root_agent = Agent(
    model=Gemini(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config),
    name="sc2_root",
    description="A helpful assistant for finance questions.",
    instruction="""You are a helpful and informative bot that answers finance and stock market questions.
    Your goal is to answer the user's question by orchestrating a workflow. Follow these rules at all times:

    RULE#1: You MUST call the `sc2_planner` tool to obtain a function call plan.
    RULE#2: Next, after receiving the plan you MUST call the `sc2_summary` tool to create a concise summary.
    RULE#3: Finally, present the final summary clearly to the user as your response.""",
    tools=[AgentTool(agent=planner_agent), AgentTool(agent=summary_agent)],
    output_key="user_interest"
)
