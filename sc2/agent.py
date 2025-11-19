from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini as LLM
from google.adk.tools import AgentTool
from src import retry_config
from src.fntool_def import *
from src.fntool import local_datetime

planner_agent = Agent(
    model=LLM(
        model="gemini-2.5-flash",
        retry_options=retry_config),
    name="sc2_planner",
    description="A highly intelligent FunctionTool call planner.",
    instruction="""
    You are a highly intelligent FunctionTool call planner. Your sole purpose is to analyze a user's request
    and generate a plan of FunctionTool calls that would be necessary to fulfill that request.

    **IMPORTANT INSTRUCTIONS:**
    1.  **DO NOT EXECUTE ANY TOOLS.** Your task is only to provide the plan.
    2.  The plan must be a JSON array of objects. Each object represents a single tool call.
    3.  Each tool call object must have three keys:
        *   `tool_name`: The exact name of the FunctionTool to be called.
        *   `args`: A dictionary containing the arguments for that tool call, mapping parameter names to their values.
        *   `thought`: A description of the reasoning behind choosing this tool with selected args.
    4.  Ensure all required parameters for each tool are included in the `args` dictionary.
    5.  If multiple steps are required, list them in the logical order of execution.
    6.  If no tools are needed to address the request, return an empty JSON array `[]`.
    7.  If the request cannot be fulfilled by the available tools, state that clearly before providing an empty array.

    **Example Plan Format:**
    ```json
    [
        {
            "tool_name": "get_symbol_1",
            "args": {
                "q": "Apple", 
                "exchange": "US,
                "query": "What is Apple's stock ticker?"
            }
        },
        {
            "tool_name": "get_market_status_1",
            "args": {
                "exchange": "US"
            }
        }
    ]
    ```
    """,
    tools=finance_tools_def,
    output_key="interest_plan"
)

summary_agent = Agent(
    model=LLM(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config),
    name="sc2_summary",
    description="An expert writer that knows HTML, JSON and Markdown.",
    instruction="""
    Read the provided interest_plan and create a concise summary.
    Follow these rules at all times:

    RULE#0: Parse interest_plan into a summary of FunctionTool calls to answer the question.
    RULE#1: Convert all timestamps to local date/time before you respond.
    RULE#2: Incorporate as much useful information in your final response.
    
    interest_plan:
    {interest_plan}""",
    tools=[local_datetime],
    output_key="interest_summary",
)

root_agent = Agent(
    model=LLM(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config),
    name="sc2_root",
    description="A helpful assistant for finance questions.",
    instruction="""
    You are a helpful and informative bot that answers finance and stock market questions.
    Your goal is to answer the user's question by orchestrating a workflow. Follow these steps at all times:

    STEP#1: You MUST call the `sc2_planner` tool to obtain a function call plan.
    STEP#2: Next you MUST call the `sc2_summary` tool to create a concise summary.
    STEP#3: Lastly, present the final summary clearly to the user as your response.""",
    tools=[AgentTool(agent=planner_agent), AgentTool(agent=summary_agent)],
    output_key="user_interest"
)
