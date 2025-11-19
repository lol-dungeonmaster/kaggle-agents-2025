from google.api_core import retry
from tqdm import tqdm
from typing import Optional
from .. import is_retriable
from .rag import RetrievalAugmentedGeneration

# Define subclass: wiki-augmented generation.
class WikiRAG(RetrievalAugmentedGeneration):
    def __init__(self, genai_client):
        super().__init__(genai_client, "wikidocs")
            
    def add_wiki_documents(self, title: str, wiki_chunks: list):
        self.embed_fn.document_mode = True # Switch to document mode.
        result = self.get_wiki_documents(title)
        if len(result) == 0:
            ids = list(map(str, range(self.db.count(), self.db.count()+len(wiki_chunks))))
            metas=[{"title": title, "source": "add_wiki_documents"}]*len(wiki_chunks)
            tqdm(self.db.add(ids=ids, documents=wiki_chunks, metadatas=metas), desc="Generate wiki embeddings")

    def get_wiki_documents(self, title: Optional[str] = None):
        self.embed_fn.document_mode = False # Switch to query mode.
        if title is None:
            return self.stored_result(self.db.get(where={"source": "add_wiki_document"}))
        else:
            return self.stored_result(self.db.get(where={"title": title}))

    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def generate_with_wiki_passages(self, query: str, title: str, passages: list[str]):
        return self.generate_answer(query, where={"title": title}, passages=passages)