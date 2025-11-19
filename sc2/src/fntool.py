from google.adk.tools import FunctionTool
from .fntool_def import FnToolDef

class FnTools(FnToolDef):

    @classmethod
    def get_symbol_1(cls, q: str, exchange: str, query: str) -> dict:
        pass # Function implementation would go here

    @classmethod
    def get_symbols_1(cls, exchange: str, query: str) -> list[dict]:
        return None # todo

    @classmethod
    def get_name_1(cls, q: str, exchange: str, query: str, company: str) -> list[dict]:
        pass # Function implementation would go here

    @classmethod
    def get_symbol_quote_1(cls, symbol: str, query: str, exchange: str) -> dict:
        pass # Function implementation would go here

    @classmethod
    def get_market_status_1(cls, exchange: str) -> dict:
        pass # Function implementation would go here

    @classmethod
    def get_market_session_1(cls, exchange: str) -> str | None:
        pass # Function implementation would go here

    @classmethod
    def get_company_peers_1(cls, symbol: str, grouping: str, exchange: str, query: str) -> dict:
        pass # Function implementation would go here

    @classmethod
    def get_local_datetime(cls, t: list[int]) -> list[str]:
        pass # Function implementation would go here

    @classmethod
    def get_last_market_close(cls, exchange: str) -> str:
        pass # Function implementation would go here

    @classmethod
    def get_exchange_codes_1(cls) -> dict[str, str]:
        pass # Function implementation would go here

    @classmethod
    def get_exchange_code_1(cls, q: str) -> str:
        pass # Function implementation would go here

    @classmethod
    def get_financials_1(cls, symbol: str, metric: str, query: str) -> dict:
        pass # Function implementation would go here

    @classmethod
    def get_daily_candlestick_2(cls, stocksTicker: str, date: str, adjusted: str, 
                                exchange: str, query: str) -> dict:
        pass # Function implementation would go here

    @classmethod
    def get_custom_candlestick_2(cls, stocksTicker: str, multiplier: int, timespan: str,
                                 from_date: str,  # Renamed 'from' to 'from_date' to avoid Python keyword conflict
                                 to_date: str,    # Renamed 'to' to 'to_date' to avoid Python keyword conflict
                                 adjusted: str, sort: str, exchange: str, query: str) -> list[dict]:
        pass # Function implementation would go here

    @classmethod
    def get_ticker_overview_2(cls, ticker: str, query: str) -> dict:
        pass # Function implementation would go here

    @classmethod
    def get_recommendation_trends_1(cls, symbol: str, query: str) -> list[dict]:
        pass # Function implementation would go here

    @classmethod
    def get_news_with_sentiment_2(cls, limit: int, ticker: str, 
                                  published_utc_gte: str,  # Renamed from 'published_utc.gte' for valid Python argument name
                                  published_utc_lte: str,  # Renamed from 'published_utc.lte' for valid Python argument name
                                  order: str, sort: str, query: str) -> list[dict]:
        pass # Function implementation would go here

    @classmethod
    def get_wiki_grounding(cls, id: str, q: str) -> str:
        pass # Function implementation would go here

    @classmethod
    def get_search_grounding(cls, q: str, id: str) -> str:
        pass # Function implementation would go here

    @classmethod
    def get_rest_grounding(cls, q: str, id: str) -> str:
        pass # Function implementation would go here

symbol_search = FunctionTool(func=FnTools.get_symbol_1)
filter_symbols = FunctionTool(func=FnTools.get_symbols_1)
symbol_name = FunctionTool(func=FnTools.get_name_1)
symbol_quote = FunctionTool(func=FnTools.get_symbol_quote_1)
market_status = FunctionTool(func=FnTools.get_market_status_1)
market_session = FunctionTool(func=FnTools.get_market_session_1)
symbol_peers = FunctionTool(func=FnTools.get_company_peers_1)
local_datetime = FunctionTool(func=FnTools.get_local_datetime)
last_market_close = FunctionTool(func=FnTools.get_last_market_close)
all_exchange_codes = FunctionTool(func=FnTools.get_exchange_codes_1)
exchange_code = FunctionTool(func=FnTools.get_exchange_code_1)
basic_financials = FunctionTool(func=FnTools.get_financials_1)
historical_candle = FunctionTool(func=FnTools.get_daily_candlestick_2)
custom_candle = FunctionTool(func=FnTools.get_custom_candlestick_2)
symbol_overview = FunctionTool(func=FnTools.get_ticker_overview_2)
symbol_trends = FunctionTool(func=FnTools.get_recommendation_trends_1)
scored_news = FunctionTool(func=FnTools.get_news_with_sentiment_2)
wiki_grounding = FunctionTool(func=FnTools.get_wiki_grounding)
search_grounding = FunctionTool(func=FnTools.get_search_grounding)
rest_grounding = FunctionTool(func=FnToolDef.get_rest_grounding)

finance_tools = [
    symbol_search, filter_symbols, symbol_name, symbol_quote,
    market_status, market_session, symbol_peers, local_datetime,
    last_market_close, all_exchange_codes, exchange_code, basic_financials,
    historical_candle, custom_candle, symbol_overview, symbol_trends,
    scored_news, wiki_grounding, search_grounding, rest_grounding
]