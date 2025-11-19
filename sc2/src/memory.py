from datetime import datetime
from google.genai import types
from basemodel import GeneratedEvent

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