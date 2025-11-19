import warnings, wikipedia
from bs4 import Tag
from langchain_text_splitters.html import HTMLSemanticPreservingSplitter
from tqdm import tqdm
from wikipedia.exceptions import DisambiguationError, PageError
from ..api import Api
from ..db.wiki import WikiRAG

# Define tool: wiki-grounding generation.
# - Creates new groundings by similarity to topic
# - Retrieves existing groundings by similarity to topic
api = NewType("Api", None) # type: ignore (forward-decl)
class WikiGroundingTool:   
    def __init__(self, genai_client):
        self.client = genai_client
        self.rag = WikiRAG(genai_client)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore") # suppress beta-warning
            self.splitter = HTMLSemanticPreservingSplitter(
                headers_to_split_on=[("h2", "Main Topic"), ("h3", "Sub Topic")],
                separators=["\n\n", "\n", ". ", "! ", "? "],
                max_chunk_size=Api.Const.ChunkMax(),
                chunk_overlap=50,
                preserve_links=True,
                preserve_images=True,
                preserve_videos=True,
                preserve_audio=True,
                elements_to_preserve=["table", "ul", "ol", "code"],
                denylist_tags=["script", "style", "head"],
                custom_handlers={"code": self.code_handler},
            )

    def generate_answer(self, query: str, topic: str):
        stored = self.rag.get_wiki_documents(topic)
        if len(stored) > 0:
            return self.rag.generate_with_wiki_passages(query, topic, [chunk.docs for chunk in stored]).text
        else:
            pages = wikipedia.search(topic + " company")
            if len(pages) > 0:
                p_topic_match = 0.80
                for i in range(len(pages)):
                    if tqdm(api.similarity([topic + " company", pages[i]]) > p_topic_match, 
                            desc= "Score wiki search by similarity to topic"):
                        page_html = Api.get(f"https://en.wikipedia.org/wiki/{pages[i]}")
                        chunks = [chunk.page_content for chunk in self.splitter.split_text(page_html)]
                        self.rag.add_wiki_documents(topic, chunks)
                        return self.rag.generate_with_wiki_passages(query, topic, chunks).text
            return Api.Const.Stop()

    def code_handler(self, element: Tag) -> str:
        data_lang = element.get("data-lang")
        code_format = f"<code:{data_lang}>{element.get_text()}</code>"
        return code_format