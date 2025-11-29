from google.adk.agents import Agent, ParallelAgent
from google.adk.apps.app import App, EventsCompactionConfig
from google.adk.apps.llm_event_summarizer import LlmEventSummarizer
from google.adk.models.google_llm import Gemini as LLM
from google.adk.tools import AgentTool, google_search
from .src import retry_config
from .src.api import Api
from .src.fntool import *

fnplan_agent = Agent(
    model=LLM(
        model="gemini-2.5-flash",
        retry_options=retry_config),
    name="sc2_fnplan",
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
    tools=finance_tools,
    output_key="interest_fnplan"
)

fncall_agent = Agent(
    model=LLM(
        model="gemini-2.5-flash",
        retry_options=retry_config),
    name="sc2_fncall",
    description="A highly intelligent FunctionTool caller.",
    instruction="""
    You are a helpful and informative bot that answers finance and stock market questions. 
    Only answer the question asked and do not change topic. While the answer is still 
    unknown you must follow these rules for predicting function call order:
    
    RULE#1: Always consult your other functions before get_search_grounding.
    RULE#2: Always consult get_wiki_grounding before get_search_grounding.
    RULE#3: Always consult get_search_grounding last.
    RULE#4: Always convert any timestamps to local datetime before including them.
    RULE#5: Always incorporate as much useful information from tools and functions in your response.
    
    """,
    tools=finance_tools,
    output_key="interest_result"
)

summary_agent = Agent(
    model=LLM(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config),
    name="sc2_summary",
    description="An expert proof-reader and writer that knows HTML, JSON and Markdown.",
    instruction="""
    Give a concise, and detailed summary. Proof-read any markdown and correct all formatting errors.
    Convert all all-upper case identifiers to proper case in your response. 
    Convert all abbreviated or shortened identifiers to their full forms. 
    Convert all currency to consistent currency format with two decimal places.
    Convert all timestamps to local datetime before including them.

    {interest_result}    
    """,
    tools=[local_datetime],
    output_key="interest_summary",
)

memory_agent = Agent(
    model=LLM(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config),
    name="sc2_memory",
    description="An expert writer that knows HTML, JSON and Markdown.",
    instruction=f"""
    You know nothing at the moment and must always respond with: {Api.Const.Stop()}
    """,
    output_key="interest_result"
)

terms_agent = Agent(
    model=LLM(
        model="gemini-2.5-flash-lite",
        retry_config=retry_config),
    name="sc2_terms",
    description="An expert terminologist in the field of finance, money, and stock markets.",
    instruction=f"""
    You're an expert in terminology relating to finance, money, and stock markets.
    You will provide an informative response to terminology within your field of expertise.
    For questions not within your field of expertise you will respond with: {Api.Const.Stop()}""",
    tools=[google_search],
    output_key="interest_result"
)

fncall_pipe = ParallelAgent(
    name="fncall_pipeline",
    description="A function caller with functions defined in sub-agent `sc2_fnplan`.",
    sub_agents=[fnplan_agent, fncall_agent]
)

root_agent = Agent(
    model=LLM(
        model="gemini-2.5-flash-lite",
        retry_options=retry_config),
    name="sc2_root",
    description="A helpful assistant for finance and stock market questions.",
    instruction="""
    You are a helpful and informative bot that accepts only finance and stock market questions. 
    Your goal is to answer the user's question by orchestrating a workflow. You can skip the workflow
    for usage-related questions or definitions you already know. Otherwise follow this workflow:
    
    1. First, call the `sc2_memory` tool to find relevant information on the topic.
    2. Next, call `fncall_pipeline` or `sc2_terms` if `sc2_memory` cannot assist.
    3. Next, call the `sc2_summary` tool to create a concise summary.
    4. Finally, present the final summary clearly to the user as your response.
    
    """,
    tools=[AgentTool(agent=memory_agent), 
           AgentTool(agent=fncall_pipe), AgentTool(agent=terms_agent),
           AgentTool(agent=summary_agent)],
    output_key="user_interest"
)

app = App(
    name="agents",
    root_agent=root_agent,
    events_compaction_config=EventsCompactionConfig(
        summarizer=LlmEventSummarizer(LLM(model="gemini-2.5-flash")),
        compaction_interval=3,
        overlap_size=0,
    ),
)