import json
from tqdm import tqdm
from rag import RetrievalAugmentedGeneration

# Define subclass: search-augmented generation.
class SearchRAG(RetrievalAugmentedGeneration):
    def __init__(self, genai_client):
        super().__init__(genai_client, "searchdocs")

    def add_grounded_document(self, query: str, topic: str, result):
        self.embed_fn.document_mode = True # Switch to document mode.
        chunks = result.candidates[0].grounding_metadata.grounding_chunks
        supports = result.candidates[0].grounding_metadata.grounding_supports
        if supports is not None: # Only add grounded documents which have supports
            grounded_text = [f"{s.segment.text}" for s in supports]
            source = [f"{c.web.title}" for c in chunks]
            score = [f"{s.confidence_scores}" for s in supports]
            tqdm(self.db.add(ids=str(self.db.count()),
                             documents=json.dumps(grounded_text),
                             metadatas=[{"source": ", ".join(source),
                                         "confidence_score": ", ".join(score),
                                         "topic": topic,
                                         "question": query}]),
                 desc="Generate grounding embedding")

    def get_grounding_documents(self, query: str, topic: str):
        self.embed_fn.document_mode = False # Switch to query mode.
        return self.stored_result(self.db.get(where={"$and": [{"question": query}, {"topic": topic}]}))