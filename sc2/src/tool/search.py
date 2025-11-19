import ast, re
from google.api_core import retry
from google.genai import types
from tqdm import tqdm
from .. import is_retriable
from ..api import Api
from ..db.search import SearchRAG

# Define tool: search-grounding generation.
# - Creates new groundings by exact match to topic
# - Retrieves existing groundings by similarity to topic
class SearchGroundingTool:
    config_ground = types.GenerateContentConfig(
        tools=[types.Tool(google_search=types.GoogleSearch())],
        temperature=0.0
    )
    
    def __init__(self, api: Api):
        self.api = api
        self.client = api.args.CLIENT
        self.rag = SearchRAG(api)

    def generate_answer(self, query: str, topic: str):
        stored = self.rag.get_grounding_documents(query, topic)
        if len(stored) > 0:
            for i in range(len(stored)):
                meta_q = stored[i].meta["question"]
                p_ground_match = 0.95 # This can be really high ~ 95-97%
                if tqdm(self.api.similarity([query, meta_q]) > p_ground_match,
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
        response = self.api.retriable(self.client.models.generate_content, 
                                      model=self.api(Api.Model.GEN), 
                                      config=self.config_ground,
                                      contents=contents)
        if response.candidates[0].grounding_metadata.grounding_supports is not None:
            if self.is_consistent(query, topic, response.text):
                self.rag.add_grounded_document(query, topic, response)
                return response.text 
        return Api.Const.Stop() # Empty grounding supports or not consistent in response

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
    
    def get_search_grounding(self, q: str, id: str):
        self.generate_answer(query=q, topic=id)