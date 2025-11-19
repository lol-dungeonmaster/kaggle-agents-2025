import ast, json, logging, os, pandas, time
from datetime import datetime, timedelta
from dateutil.parser import parse
from google.api_core import retry
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters.json import RecursiveJsonSplitter
from pydantic import BaseModel
from tqdm import tqdm
from typing import Optional
from .. import is_retriable
from ..api import Api
from ..basemodel import ChromaDBResult, GeneratedEvent, MarketEvent, MarketSession
from .rag import RetrievalAugmentedGeneration

# Define subclass: rest-augmented generation.
class RestRAG(RetrievalAugmentedGeneration):
    exchange_codes: Optional[dict] = None
    exchange_lists: dict = {}
    events: dict = {}
    holidays: dict = {}

    def __init__(self, api: Api):
        super().__init__(api, "restdocs")
        logging.getLogger("chromadb").setLevel(logging.ERROR) # suppress warning on existing id
        self.add_exchanges_data()
        self.set_holidays("US", ["09-01-2025","10-13-2025","11-11-2025","11-27-2025","12-25-2025"])
        self.generated_events("US")

    def add_exchanges_data(self):
        try:
            df = pandas.read_csv("/kaggle/input/exchanges/exchanges_src.csv") if os.getenv("KAGGLE_KERNEL_RUN_TYPE") else pandas.read_csv("exchanges_src.csv")
        except FileNotFoundError as e:
            print("restrag.add_exchanges_data: file not found")
        df = df.drop(["close_date"], axis=1).fillna("")
        df.to_csv("exchanges.csv", index=False)
        exchanges = CSVLoader(file_path="exchanges.csv", encoding="utf-8", csv_args={"delimiter": ","}).load()
        self.add_documents_list(exchanges)

    def set_holidays(self, exchange_code: str, holidays: list):
        self.holidays[exchange_code] = [datetime.strptime(h, "%m-%d-%Y").date() for h in holidays]

    def get_exchange_codes(self, with_query: Optional[str] = None):
        gen = None
        if with_query and with_query not in self.exchange_lists.keys():
            gen = tqdm(total=1, desc="Generate exchange codes with_query")
            data = self.get_exchanges_csv(
                f"""What is the {with_query} exchange code? Return only the exchange codes 
                as a list in string form. Just the list string. 
                Omit all other information or details. Do not chat or use sentences.""").candidates[0].content
            self.exchange_lists[with_query] = ast.literal_eval(data.parts[-1].text)
        elif with_query is None and self.exchange_codes is None:
            gen = tqdm(total=1, desc="Generate exchange codes")
            data = self.get_exchanges_csv(
                """Give me a dictionary in string form. It must contain key:value pairs 
                mapping exchange code to name. Just the dictionary string. 
                Omit all other information or details. Do not chat or use sentences.""").candidates[0].content
            self.exchange_codes = ast.literal_eval(data.parts[-1].text.strip("\\`"))
        if gen:
            gen.update(1)
        return self.exchange_lists[with_query] if with_query else self.exchange_codes

    def get_event_date(self, event_t: str, exchange_code: str, event: MarketEvent):
        current_dt_str = datetime.now(GeneratedEvent.tz()).strftime('%c')
        current_dt = datetime.strptime(current_dt_str, "%a %b %d %H:%M:%S %Y")
        current_t_str = datetime.now(GeneratedEvent.tz()).strftime('%H:%M:%S')
        current_t = datetime.strptime(current_t_str, "%H:%M:%S").time()
        event_time = parse(event_t).time()
        gen_datetime = None
        if event is MarketEvent.LAST_CLOSE:
            last_close_day = current_dt.date() - timedelta(days=0 if current_t > event_time else 1)
            # Loop backwards to find the last valid trading day (not a weekend or holiday).
            while last_close_day.weekday() >= 5 or last_close_day in self.holidays[exchange_code]: # 5 = Sat, 6 = Sun
                last_close_day -= timedelta(days=1)
            # Combine the date and time.
            gen_datetime = datetime.combine(last_close_day, event_time)
        else:
            next_event_day = current_dt.date() + timedelta(days=0 if current_t < event_time else 1)
            # Loop forward to find the next valid trading day (not a weekend or holiday).
            while next_event_day.weekday() >= 5 or next_event_day in self.holidays[exchange_code]: # 5 = Sat, 6 = Sun
                next_event_day += timedelta(days=1)
            # Combine date and time.
            gen_datetime = datetime.combine(next_event_day, event_time)
        # Format the result as requested.
        return gen_datetime.strftime('%a %b %d %X %Y')

    def generate_event(self, exchange_code: str, event: MarketEvent):
        if event is MarketEvent.LAST_CLOSE or event is MarketEvent.POST_CLOSE:
            prompt = f"""What is the closing time including post_market hours."""
        elif event is MarketEvent.PRE_OPEN or event is MarketEvent.REG_OPEN:
            is_pre = "including" if event is MarketEvent.PRE_OPEN else "excluding"
            prompt = f"""What is the opening time {is_pre} pre_market hours."""
        elif event is MarketEvent.REG_CLOSE:
            prompt = f"""What is the closing time excluding post_market hours."""
        prompt = f"""Answer based on your knowledge of exchange operating hours.
            Do not answer in full sentences. Omit all chat and provide the answer only.
            The fields pre_market and post_market both represent extended operating hours.

            The current date and time: {datetime.now(GeneratedEvent.tz()).strftime('%c')}
            
            Consider the {exchange_code} exchange's operating hours.
            {prompt}
            
            Answer with the time in this format: '%H:%M:%S'.
            Omit all other chat and details. Do not use sentences."""
        progress = tqdm(total=1, desc=f"Generate {exchange_code}->{event}")
        response = self.get_exchanges_csv(prompt).candidates[0].content
        if Api.Const.Stop() in f"{response.parts[-1].text}":
            progress.close()
            self.api.generation_fail()
            time.sleep(self.api.dt_between)
            return self.generate_event(exchange_code, event)
        else:
            response = self.get_event_date(response.parts[-1].text, exchange_code, event)
            progress.update(1)
            return response

    def generated_events(self, exchange_code: str) -> GeneratedEvent:
        # Check for an existing GeneratedEvent object having updates.
        if exchange_code in self.events.keys() and self.events[exchange_code].has_update():
            event_obj = self.events[exchange_code]
            event_state = [(event_obj.pre_open, MarketEvent.PRE_OPEN),
                           (event_obj.reg_open, MarketEvent.REG_OPEN),
                           (event_obj.reg_close, MarketEvent.REG_CLOSE),
                           (event_obj.post_close, MarketEvent.POST_CLOSE)]
            # Need now in same format as generated.
            datetime_now = parse(datetime.now(event_obj.tz()).strftime('%c'))
            gen_ts = parse(event_obj.timestamp)
            # Re-generate events when day changes.
            if datetime_now.day > gen_ts.day:
                del self.events[exchange_code]
                return self.generated_events(exchange_code)
            # Update changed events on trading days.
            for e in event_state:
                if datetime_now > parse(e[0]):
                    event_dt = self.generate_event(exchange_code, e[1])
                    match e[1]:
                        case MarketEvent.PRE_OPEN:
                            event_obj.pre_open = event_dt
                        case MarketEvent.REG_OPEN:
                            event_obj.reg_open = event_dt
                        case MarketEvent.REG_CLOSE:
                            event_obj.reg_close = event_dt
                        case MarketEvent.POST_CLOSE:
                            event_obj.post_close = event_dt
            event_obj.timestamp = datetime.now(event_obj.tz()).strftime('%c')
            self.events[exchange_code] = event_obj
        # Generate events for an exchange code not in cache.
        elif exchange_code not in self.events.keys():
            self.events[exchange_code] = GeneratedEvent(
                last_close=self.generate_event(exchange_code, MarketEvent.LAST_CLOSE),
                pre_open=self.generate_event(exchange_code, MarketEvent.PRE_OPEN),
                reg_open=self.generate_event(exchange_code, MarketEvent.REG_OPEN),
                reg_close=self.generate_event(exchange_code, MarketEvent.REG_CLOSE),
                post_close=self.generate_event(exchange_code, MarketEvent.POST_CLOSE),
                is_holiday=datetime.now().date() in self.holidays[exchange_code])
        return self.events[exchange_code]

    def set_holiday_event(self, exchange_code: str):
        self.generated_events(exchange_code).is_holiday = True

    def last_market_close(self, exchange_code: str):
        return self.generated_events(exchange_code).last_close

    def add_api_document(self, query: str, api_response: str, topic: str, source: str = "add_api_document"):
        self.embed_fn.document_mode = True # Switch to document mode.
        splitter = RecursiveJsonSplitter(max_chunk_size=Api.Const.ChunkMax())
        docs = splitter.create_documents(texts=[api_response], convert_lists=True)
        ids = list(map(str, range(self.db.count(), self.db.count()+len(docs))))
        content = [json.dumps(doc.page_content) for doc in docs]
        metas = [{"source": source, "topic": topic}]*len(docs)
        tqdm(self.db.add(ids=ids, documents=content, metadatas=metas), desc="Generate api embedding")

    def add_peers_document(self, query: str, names: list, topic: str, source: str, group: str):
        self.embed_fn.document_mode = True # Switch to document mode.
        peers = {"symbol": topic, "peers": names}
        tqdm(self.db.add(ids=str(self.db.count()),
                         documents=[json.dumps(peers)],
                         metadatas=[{"source": source, "topic": topic, "group": group}]),
             desc="Generate peers embedding")

    def get_peers_document(self, query: str, topic: str, group: str):
        return self.get_documents_list(query, where={"$and": [{"group": group}, {"topic": topic}]})

    def add_rest_chunks(self, chunks: list, topic: str, source: str, ids: Optional[list[str]] = None,
                        meta_opt: Optional[list[dict]] = None, is_update: bool = True):
        self.embed_fn.document_mode = True # Switch to document mode
        if ids is None:
            ids = list(map(str, range(self.db.count(), self.db.count()+len(chunks))))
        if isinstance(chunks[0], BaseModel):
            docs = [model.model_dump_json() for model in chunks]
        else:
            docs = [json.dumps(obj) for obj in chunks]
        meta_base = {"source": source, "topic": topic}
        if meta_opt is not None:
            for m in meta_opt:
                m.update(meta_base)
        metas = [meta_base]*len(chunks) if meta_opt is None else meta_opt
        if is_update:
            tqdm(self.db.upsert(ids=ids, documents=docs, metadatas=metas), desc="Upsert chunks embedding")
        else:
            tqdm(self.db.add(ids=ids, documents=docs, metadatas=metas), desc="Add chunks embedding")

    def get_market_status(self, exchange_code: str) -> tuple[list[ChromaDBResult], bool]: # result, has rest update
        self.embed_fn.document_mode = False # Switch to query mode.
        stored = self.stored_result(self.db.get(where={
            "$and": [{"exchange": exchange_code}, {"topic": "market_status"}]}))
        if len(stored) == 0:
            return stored, True
        # Check for a daily market status update.
        status = json.loads(stored[0].docs)
        gen_day = parse(self.generated_events(exchange_code).timestamp).day
        store_day = parse(stored[0].meta['timestamp']).day
        if status["holiday"] != MarketSession.NA.value and gen_day == store_day:
            return stored, False
        elif gen_day > store_day:
            return stored, True
        # Update with generated events to avoid rest api requests.
        status["session"] = self.generated_events(exchange_code).session().value
        status["isOpen"] = self.generated_events(exchange_code).is_open()
        stored[0].docs = json.dumps(status)
        return stored, False

    def get_basic_financials(self, query: str, topic: str, source: str = "get_financials_1"):
        return self.get_documents_list(
            query, max_sources=200, where={"$and": [{"source": source}, {"topic": topic}]})

    def add_quote_document(self, query: str, quote: str, topic: str, timestamp: int, source: str):
        self.embed_fn.document_mode = True # Switch to document mode.
        tqdm(self.db.add(ids=str(self.db.count()), 
                             documents=[quote], 
                             metadatas=[{"source": source, "topic": topic, "timestamp": timestamp}]), 
             desc="Generate quote embedding")

    def get_api_documents(self, query: str, topic: str, source: str = "add_api_document", 
                          meta_opt: Optional[list[dict]] = None):
        where = [{"source": source}, {"topic": topic}]
        if meta_opt is None:
            return self.get_documents_list(query, where={"$and": where})
        else:
            for meta in meta_opt:
                for k,v in meta.items():
                    where.append({k: v})
            return self.get_documents_list(query, where={"$and": where})

    def query_api_documents(self, query: str, topic: str, source: str = "add_api_document"):
        return self.generate_answer(query, where={"$and": [{"source": source}, {"topic": topic}]})

    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def get_exchanges_csv(self, query: str):
        return self.generate_answer(query, max_sources=100, where={"source": "exchanges.csv"})