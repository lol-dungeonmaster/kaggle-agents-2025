from datetime import datetime
from typing import Optional
from tqdm import tqdm
from ..api import Api
from ..basemodel import GeneratedEvent
from .rag import RetrievalAugmentedGeneration

class MemoryService(RetrievalAugmentedGeneration):
    def __init__(self, api: Api):
        super().__init__(api, "memory_service", similarity_task=True)

    def add_memory(self, key: str, value: str) -> str:
        """Create a memory in key-value format.

        Adds the memory by key or updates it with value.

        Args:
            key: A topic (key) within the key-value store. It must be short 
                 and abstract a general attribute or preference.
            value: The memory describing the topic's answer in full and descriptive
                   sentences. Includes role-designation and/or the key content.
        
        Returns:
            The memory (value).
        """
        progress = tqdm(total=1, desc=f"Generate memory embedding ({key})")
        dt_now = datetime.now(GeneratedEvent.tz()).strftime('%c')
        self.db.upsert(ids=[key], 
                       documents=[value], 
                       metadatas=[{"key": key, "date": dt_now}])
        progress.update(1)
        return value

    def get_memory(self, key: str) -> Optional[str]:
        """Recall a memory (value) using it's key.

        Recalls the memory (value) associated with the provided key.

        Args:
            key: A topic (key) within the key-value store.

        Returns:
            The memory (value) associated with the provided key, or None.
        """
        stored = self.stored_result(self.db.get(ids=[key]))
        return stored[0].docs if stored else None
    
    def topic_search(self, question: str) -> str:
        f"""Search for a memory by topic.

        Searches for a memory about question within the key-value store.

        Args:
            question: The question to be answered by values within the key-value store.

        Returns:
            The memory (str) answering question, or {Api.Const.Stop()}.
        """
        return self.generate_answer(question, max_sources=2).text