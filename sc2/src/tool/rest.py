import json, time
from enum import Enum
from google.api_core import retry
from pydantic import BaseModel
from threading import Timer
from tqdm import tqdm
from typing import Optional, Callable
from ..api import Api
from ..basemodel import *
from ..db.rest import RestRAG
from ..fntool_def import RestFnDef
from ..secret import UserSecretsClient

# Rest api-helpers to manage request-per-minute limits.
# - define an entry for each endpoint limit
# - init rest tool with limits to create blocking queues
# - apply a limit to requests with rest_tool.try_url
class ApiLimit(Enum):
    FINN = "finnhub.io",50
    POLY = "polygon.io",4 # (id_url,rpm)

class BlockingUrlQueue:
    on_cooldown = False
    cooldown = None
    cooldown_start = None
    
    def __init__(self, rest_fn: Callable, per_minute: int):
        self.per_minute_max = per_minute
        self.quota = per_minute
        self.rest_fn = rest_fn

    def push(self, rest_url: str):
        if not self.on_cooldown:
            self.cooldown = Timer(60, self.reset_quota)
            self.cooldown.start()
            self.cooldown_start = time.time()
            self.on_cooldown = True
        if self.quota > 0:
            self.quota -= 1
            time.sleep(0.034) # ~30 requests per second
            return self.rest_fn(rest_url)
        else:
            print(f"limited {self.per_minute_max}/min, waiting {self.limit_expiry()}s")
            time.sleep(max(self.limit_expiry(),0.5))
            return self.push(rest_url)

    def reset_quota(self):
        self.quota = self.per_minute_max
        self.on_cooldown = False
        self.cooldown_start = None

    def limit_expiry(self):
        if self.cooldown_start:
            return max(60-(time.time()-self.cooldown_start),0)
        return 0

# Define tool: rest-grounding generation.
# - Parses the json response from rest api's
# - Prevents concurrent http requests
class RestGroundingTool(RestFnDef):
    limits = None

    def __init__(self, api: Api, with_limits: bool):
        self.api = api
        self.client = api.args.CLIENT
        self.rag = RestRAG(api)
        self.MASS_AUTH = UserSecretsClient().get_secret("POLYGON_API_KEY") # todo: check this throws on kaggle
        self.FINN_AUTH = UserSecretsClient().get_secret("FINNHUB_API_KEY")
        if with_limits:
            self.limits = {}
            for rest_api in ApiLimit:
                self.limits[rest_api.value[0]] = BlockingUrlQueue(Api.get, rest_api.value[1])

    def get_limit(self, rest_api: ApiLimit) -> Optional[BlockingUrlQueue]:
        return self.limits[rest_api.value[0]] if self.limits else None

    def basemodel(self, data: str, schema: BaseModel, from_lambda: bool = False) -> Optional[BaseModel]:
        try:
            if from_lambda:
                return schema(results=json.loads(data))
            return schema.model_validate_json(data)
        except Exception as e:
            raise e

    def dailycandle(self, data: str) -> Optional[DailyCandle]:
        try:
            candle = json.loads(data)
            if "from" not in candle:
                raise ValueError("not a dailycandle / missing value for date")
            agg = self.basemodel(data, Aggregate)
            return DailyCandle(from_date=candle["from"], 
                               status=agg.status.value, 
                               symbol=agg.symbol, 
                               open=agg.open, 
                               high=agg.high, 
                               low=agg.low, 
                               close=agg.close, 
                               volume=agg.volume, 
                               otc=agg.otc, 
                               preMarket=agg.preMarket, 
                               afterHours=agg.afterHours)
        except Exception as e:
            raise e

    @retry.Retry(timeout=600)
    def try_url(self, url: str, schema: BaseModel, as_lambda: bool, with_limit: Optional[BlockingUrlQueue],
                success_fn: Callable, *args, **kwargs):
        try:
            if self.limits is None:
                data = Api.get(url)
            elif with_limit:
                data = with_limit.push(url)
            if schema is DailyCandle:
                model = self.dailycandle(data)
            else:
                model = self.basemodel(data, schema, as_lambda)
        except Exception as e:
            try:
                print(f"try_url exception: {e}")
                if issubclass(schema, RestResultPoly):
                    return success_fn(*args, **kwargs, result=self.basemodel(data, RestResultPoly))
            except Exception as not_a_result:
                print(not_a_result)
            return Api.Const.Stop()
        else:
            return success_fn(*args, **kwargs, model=model)

    def get_symbol_matches(self, with_content, by_name: bool, model: SymbolResult):
        matches = []
        max_failed_match = model.count if not by_name else 3
        p_desc_match = 0.92
        p_symb_match = 0.95
        if model.count > 0:
            for obj in tqdm(model.get(), desc="Score similarity to query"):
                if max_failed_match > 0:
                    desc = [with_content["q"].upper(), obj.description.split("-", -1)[0]]
                    symb = [with_content["q"].upper(), obj.symbol]
                    if by_name and self.api.similarity(desc) > p_desc_match: 
                        matches.append(obj.symbol)
                    elif not by_name and self.api.similarity(symb) > p_symb_match:
                        matches.append(obj.description)
                        max_failed_match = 0
                    else:
                        max_failed_match -= 1
        if len(matches) > 0:
            self.rag.add_api_document(with_content["query"], matches, with_content["q"], "get_symbol_1")
            return matches
        return Api.Const.Stop()

    def get_quote(self, with_content, model: Quote):
        quote = model.model_dump_json()
        self.rag.add_quote_document(with_content["query"], quote, with_content["symbol"], model.t, "get_quote_1")
        return quote

    def parse_financials(self, with_content, model: BasicFinancials):
        metric = list(model.metric.items())
        chunks = []
        # Chunk the metric data.
        for i in range(0, len(metric), Api.Const.MetricBatch()):
            batch = metric[i:i + Api.Const.MetricBatch()]
            chunks.append({"question": with_content["query"], "answer": batch})
        # Chunk the series data.
        for key in model.series.keys():
            series = list(model.series[key].items())
            for s in series:
                if self.api.token_count(s) <= Api.Const.ChunkMax():
                    chunks.append({"question": with_content["query"], "answer": s})
                else:
                    k = s[0]
                    v = s[1]
                    for i in range(0, len(v), Api.Const.SeriesBatch()):
                        batch = v[i:i + Api.Const.SeriesBatch()]
                        chunks.append({"question": with_content["query"], "answer": {k: batch}})
        self.rag.add_rest_chunks(chunks, topic=with_content["symbol"], source="get_financials_1")
        return chunks

    def parse_news(self, with_content, model: NewsResultFinn):
        if model.count > 0:
            metas = []
            for digest in model.get():
                pub_date = datetime.fromtimestamp(digest.datetime, tz=GeneratedEvent.tz()).strftime("%Y-%m-%d")
                metas.append({"publisher": digest.source,
                              "published_est": parse(pub_date).timestamp(),
                              "news_id": digest.id,
                              "related": digest.related})
            self.rag.add_rest_chunks(model.get(), topic=with_content["symbol"], source="get_news_1",
                                     ids=[f"{digest.id}+news" for digest in model.get()],
                                     meta_opt=metas, is_update=False)
            return [digest.summary().model_dump_json() for digest in model.get()]
        return Api.Const.Stop()

    def parse_news(self, with_content, model: Optional[NewsResultPoly] = None,
                   result: Optional[RestResultPoly] = None) -> tuple[list, str]: # list of summary, next list url
        if model and model.status in [RestStatus.OK, RestStatus.DELAY]:
            metas = []
            for news in model.get():
                pub_date = parse(news.published_utc).strftime("%Y-%m-%d")
                metas.append({"publisher": news.publisher.name,
                              "published_utc": parse(pub_date).timestamp(),
                              "news_id": news.id,
                              "related": json.dumps(news.tickers),
                              "keywords": json.dumps(news.keywords)})
            self.rag.add_rest_chunks(model.get(), topic=with_content["ticker"], source="get_news_2",
                                     ids=[news.id for news in model.get()],
                                     meta_opt=metas, is_update=False)
            return [news.summary().model_dump_json() for news in model.get()], model.next_url
        elif result:
            return result.model_dump_json()

    def parse_daily_candle(self, with_content, model: Optional[DailyCandle] = None,
                           result: Optional[RestResultPoly] = None):
        if model and model.status in [RestStatus.OK, RestStatus.DELAY]:
            self.rag.add_rest_chunks(
                chunks=[model],
                topic=with_content["stocksTicker"],
                source="daily_candle_2",
                meta_opt=[{"from_date": model.from_date, "adjusted": with_content["adjusted"]}])
            return model
        elif result:
            return result

    def parse_custom_candle(self, with_content, model: Optional[CustomCandle] = None,
                            result: Optional[RestResultPoly] = None):
        if model and model.status in [RestStatus.OK, RestStatus.DELAY]:
            metas = [{
                "timespan": with_content["timespan"],
                "adjusted": with_content["adjusted"],
                "from": with_content["from_date"],
                "to": with_content["to_date"]}]*model.count
            candles = [candle.model_dump_json() for candle in model.get()]
            self.rag.add_rest_chunks(
                chunks=candles,
                topic=with_content["stocksTicker"],
                source="custom_candle_2",
                meta_opt=metas)
            return candles
        elif result:
            return result.model_dump_json()

    def parse_overview(self, with_content, model: OverviewResult):
        overview = [model.get().model_dump_json()]
        self.rag.add_rest_chunks(chunks=overview, topic=with_content["ticker"], source="ticker_overview_2")
        return overview

    def parse_trends(self, with_content, model: TrendsResult):
        if model.count > 0:
            metas = [{"period": trend.period} for trend in model.get()]
            trends = [trend.model_dump_json() for trend in model.get()]
            self.rag.add_rest_chunks(trends, topic=with_content["symbol"], source="trends_1", meta_opt=metas)
            return trends
        return Api.Const.Stop()

    def augment_market_status(self, with_id: Optional[str], model: MarketStatusResult):
        if model.get().holiday != MarketSession.NA.value:
            self.rag.set_holiday_event(model.get().exchange)
        events = self.rag.generated_events(model.get().exchange)
        model.get().session = events.session()
        model.get().isOpen = events.is_open()
        meta = {"exchange": model.get().exchange,
                "last_close": events.last_close,
                "pre_open": events.pre_open,
                "reg_open": events.reg_open,
                "reg_close": events.reg_close,
                "post_close": events.post_close,
                "timestamp": events.timestamp }
        self.rag.add_rest_chunks([model.get()],
                                 topic="market_status",
                                 source="get_market_status_1",
                                 ids=[with_id] if with_id else None,
                                 meta_opt=[meta])
        return model.get().model_dump_json()

    def get_symbol(self, content, by_name: bool = True):
        return self.try_url(
            f"https://finnhub.io/api/v1/search?q={content['q']}&exchange={content['exchange']}&token={self.FINN_AUTH}",
            schema=SymbolResult,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.get_symbol_matches,
            with_content=content,
            by_name=by_name)

    def get_current_price(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/quote?symbol={content['symbol']}&token={self.FINN_AUTH}",
            schema=Quote,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.get_quote,
            with_content=content)

    def get_market_status(self, content, store_id: Optional[str] = None):
        return self.try_url(
            f"https://finnhub.io/api/v1/stock/market-status?exchange={content['exchange']}&token={self.FINN_AUTH}",
            schema=MarketStatusResult,
            as_lambda=True,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.augment_market_status,
            with_id=store_id)

    def get_peers(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/stock/peers?symbol={content['symbol']}&grouping={content['grouping']}&token={self.FINN_AUTH}",
            schema=PeersResult,
            as_lambda=True,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=lambda model: model)

    def get_basic_financials(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/stock/metric?symbol={content['symbol']}&metric={content['metric']}&token={self.FINN_AUTH}",
            schema=BasicFinancials,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.parse_financials,
            with_content=content)

    def get_news_simple(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/company-news?symbol={content['symbol']}&from={content['from']}&to={content['to']}&token={self.FINN_AUTH}",
            schema=NewsResultFinn,
            as_lambda=True,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.parse_news,
            with_content=content)

    def get_news_tagged(self, content):
        next_url = f"https://api.polygon.io/v2/reference/news?ticker={content['ticker']}&published_utc.gte={content['published_utc.gte']}&published_utc.lte={content['published_utc.lte']}&order={content['order']}&limit={content['limit']}&sort={content['sort']}&apiKey={self.MASS_AUTH}"
        news = []
        while True:
            news_list, next_url = self.try_url(
                next_url,
                schema=NewsResultPoly,
                as_lambda=False,
                with_limit=self.get_limit(ApiLimit.POLY),
                success_fn=self.parse_news,
                with_content=content)
            news += news_list
            if next_url is None:
                break
            next_url += f"&apiKey={self.MASS_AUTH}"
        return news

    def get_daily_candle(self, content):
        return self.try_url(
            f"https://api.polygon.io/v1/open-close/{content['stocksTicker']}/{content['date']}?adjusted={content['adjusted']}&apiKey={self.MASS_AUTH}",
            schema=DailyCandle,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.POLY),
            success_fn=self.parse_daily_candle,
            with_content=content)

    def get_custom_candle(self, content):
        return self.try_url(
            f"https://api.polygon.io/v2/aggs/ticker/{content['stocksTicker']}/range/{content['multiplier']}/{content['timespan']}/{content['from_date']}/{content['to_date']}?adjusted={content['adjusted']}&sort={content['sort']}&limit={content['limit']}&apiKey={self.MASS_AUTH}",
            schema=CustomCandle,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.POLY),
            success_fn=self.parse_custom_candle,
            with_content=content)

    def get_overview(self, content):
        return self.try_url(
            f"https://api.polygon.io/v3/reference/tickers/{content['ticker']}?apiKey={self.MASS_AUTH}",
            schema=OverviewResult,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.POLY),
            success_fn=self.parse_overview,
            with_content=content)

    def get_trends_simple(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/stock/recommendation?symbol={content['symbol']}&token={self.FINN_AUTH}",
            schema=TrendsResult,
            as_lambda=True,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.parse_trends,
            with_content=content)
    
    def get_symbol_1(self, q: str, exchange: str, query: str, by_name: bool = True):
        stored = self.rag.get_api_documents(query, q, "get_symbol_1")
        if len(stored) == 0:
            return self.get_symbol(locals(), by_name)
        return json.loads(stored[0].docs)

    def get_symbols_1(self, exchange: str, query: str) -> list[dict]:
        return None # todo

    def get_name_1(self, q: str, exchange: str, query: str):
        return self.get_symbol_1(q, exchange, query, by_name = False)

    def get_symbol_quote_1(self, symbol: str, query: str, exchange: str):
        stored = self.rag.get_api_documents(query, symbol, "get_quote_1")
        if self.rag.generated_events(exchange).is_open():
            return self.get_current_price(locals())
        elif len(stored) > 0:
            last_close = parse(self.rag.last_market_close(exchange)).timestamp()
            for quote in stored:
                if quote.meta["timestamp"] >= last_close:
                    return [quote.docs for quote in stored]
        return self.get_current_price(locals())

    def get_market_status_1(self, exchange: str) -> dict:
        stored, has_update = self.rag.get_market_status(exchange)
        if has_update:
            with_id = stored[0].store_id if len(stored) > 0 else None
            return self.get_market_status(locals(), with_id)
        return stored[0].docs

    def get_market_session_1(self, exchange: str) -> str | None:
        return json.loads(self.get_market_status_1(exchange))["session"]

    def get_company_peers_1(self, symbol: str, grouping: str, exchange: str, query: str) -> dict:
        stored = self.rag.get_peers_document(query, symbol, grouping)
        if len(stored) == 0:
            peers = self.get_peers(locals())
            if peers.count > 0:
                names = []
                for peer in peers.get():
                    if peer == symbol:
                        continue # skip including the query symbol in peers
                    name = self.get_name_1(dict(q=peer, exchange=exchange, query=query))
                    if name != Api.Const.Stop():
                        data = {"symbol": peer, "name": name}
                        names.append(data)
                self.rag.add_peers_document(query, names, symbol, "get_peers_1", grouping)
                return names
            return Api.Const.Stop()
        return json.loads(stored[0].docs)["peers"]

    def get_last_market_close(self, exchange: str) -> str:
        return self.rag.last_market_close(exchange)

    def get_exchange_codes_1(self) -> dict[str, str]:
        return self.rag.get_exchange_codes()

    def get_exchange_code_1(self, q: str) -> str:
        return self.rag.get_exchange_codes(with_query=q)

    def get_financials_1(self, symbol: str, metric: str, query: str) -> dict:
        stored = self.rag.get_basic_financials(query, symbol, "get_financials_1")
        if len(stored) == 0:
            return self.get_basic_financials(locals())
        return [chunk.docs for chunk in stored]

    def get_daily_candlestick_2(self, stocksTicker: str, from_date: str, adjusted: str, 
                                exchange: str, query: str) -> dict:
        stored = self.rag.get_api_documents(
            query=query, topic=stocksTicker, source="daily_candle_2", 
            meta_opt=[{"from_date": from_date, "adjusted": adjusted}])
        if len(stored) == 0:
            candle = self.rest.get_daily_candle(locals())
            # Attempt to recover from choosing a holiday.
            candle_date = parse(from_date)
            if candle.status is RestStatus.NONE and candle_date.weekday() == 0 or candle_date.weekday() == 4:
                content = dict(locals())
                if candle_date.weekday() == 0: # index 0 is monday, index 4 is friday
                    content["from_date"] = candle_date.replace(day=candle_date.day-3).strftime("%Y-%m-%d")
                else:
                    content["from_date"] = candle_date.replace(day=candle_date.day-1).strftime("%Y-%m-%d")
                return self.get_daily_candlestick_2(**content)
            return candle.model_dump_json()
        return [json.loads(candle.docs) for candle in stored]

    def get_custom_candlestick_2(self, stocksTicker: str, multiplier: int, timespan: str,
                                 from_date: str,  # Renamed 'from' to 'from_date' to avoid Python keyword conflict
                                 to_date: str,    # Renamed 'to' to 'to_date' to avoid Python keyword conflict
                                 adjusted: str, sort: str, limit: str, exchange: str, query: str) -> list[dict]:
        stored = self.rag.get_api_documents(
            query=query, topic=stocksTicker, source="custom_candle_2", 
            meta_opt=[{
                "timespan": timespan,
                "adjusted": adjusted,
                "from": from_date,
                "to": to_date}])
        if len(stored) == 0:
            return self.get_custom_candle(locals())
        return [json.loads(candle.docs) for candle in stored]

    def get_ticker_overview_2(self, ticker: str, query: str) -> dict:
        stored = self.rag.get_api_documents(query, ticker, "ticker_overview_2")
        if len(stored) == 0:
            return self.get_overview(locals())
        return json.loads(stored[0].docs)

    def get_recommendation_trends_1(self, symbol: str, query: str) -> list[dict]:
        stored = self.rag.get_api_documents(query, symbol, "trends_1")
        if len(stored) == 0:
            return self.get_trends_simple(locals())
        return [json.loads(trend.docs) for trend in stored]

    def get_news_with_sentiment_2(self, limit: int, ticker: str, 
                                  published_utc_gte: str,  # Renamed from 'published_utc.gte' for valid Python argument name
                                  published_utc_lte: str,  # Renamed from 'published_utc.lte' for valid Python argument name
                                  order: str, sort: str, query: str) -> list[dict]:
        timestamp_from = parse(published_utc_gte).timestamp()
        timestamp_to = parse(published_utc_lte).timestamp()
        news_from = self.rag.get_api_documents(
            query, ticker, "get_news_2", [{"published_utc": timestamp_from}])
        news_to = self.rag.get_api_documents(
            query, ticker, "get_news_2", [{"published_utc": timestamp_to}])
        if len(news_from) > 0 and len(news_to) > 0:
            stored = self.rag.get_api_documents(
                query, ticker, "get_news_2",
                [{"published_utc": {"$gte": timestamp_from}},
                {"published_utc": {"$lte": timestamp_to}}])
            return [NewsTypePoly.model_validate_json(news.docs).summary().model_dump_json() for news in stored]
        return self.get_news_tagged(locals())