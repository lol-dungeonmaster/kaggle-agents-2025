from typing import Optional
from tqdm import tqdm
from .. import log
from ..api import Api
from .rag import RetrievalAugmentedGeneration

class MemoryService(RetrievalAugmentedGeneration):
    def __init__(self, api: Api):
        super().__init__(api, "memory_service", similarity_task=True)

    def add_memory(self, key: str, value: str):
        progress = tqdm(total=1, desc=f"Generate memory embedding ({key})")
        self.db.upsert(ids=[key], documents=[value], metadatas=[{"key": key}])
        progress.update(1)

    def get_memory(self, key: str) -> Optional[str]:
        stored = self.stored_result(self.db.get(ids=[key]))
        if len(stored) != 1:
            log.info(f"get_memory: found ({len(stored)}) for key={key}")
        return stored[0].docs if stored else None
        