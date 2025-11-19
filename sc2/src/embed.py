import pandas
from chromadb import Documents, Embeddings
from google.api_core import retry
from google.genai import types, errors
from typing import NewType
from .api import Api

is_retriable = lambda e: (isinstance(e, errors.APIError) and e.code in {429, 503, 500})

# Define the embedding function.
api = NewType("Api", None) # type: ignore (forward-decl)
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
            model=api(Api.Model.EMB),
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
            for i in range(0, len(input), Api.Const.EmbedBatch()):  # Gemini max-batch-size is 100.
                response += self.__embed__(input[i:i + Api.Const.EmbedBatch()])
            return response
        except Exception as e:
            print(f"caught exception of type {type(e)}\n{e}")
            raise e

    def sts(self, content: list) -> float:
        df = pandas.DataFrame(self(content), index=content)
        score = df @ df.T
        return score.iloc[0].iloc[1]