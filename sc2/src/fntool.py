from google.adk.tools import FunctionTool
from . import RGT, SGT, WGT
from .tool.date import DateFormatTool

symbol_search = FunctionTool(func=RGT.get_symbol_1)
filter_symbols = FunctionTool(func=RGT.get_symbols_1)
symbol_name = FunctionTool(func=RGT.get_name_1)
symbol_quote = FunctionTool(func=RGT.get_symbol_quote_1)
market_status = FunctionTool(func=RGT.get_market_status_1)
market_session = FunctionTool(func=RGT.get_market_session_1)
symbol_peers = FunctionTool(func=RGT.get_company_peers_1)
local_datetime = FunctionTool(func=DateFormatTool.get_local_datetime)
last_market_close = FunctionTool(func=RGT.get_last_market_close)
all_exchange_codes = FunctionTool(func=RGT.get_exchange_codes_1)
exchange_code = FunctionTool(func=RGT.get_exchange_code_1)
basic_financials = FunctionTool(func=RGT.get_financials_1)
historical_candle = FunctionTool(func=RGT.get_daily_candlestick_2)
custom_candle = FunctionTool(func=RGT.get_custom_candlestick_2)
symbol_overview = FunctionTool(func=RGT.get_ticker_overview_2)
symbol_trends = FunctionTool(func=RGT.get_recommendation_trends_1)
scored_news = FunctionTool(func=RGT.get_news_with_sentiment_2)
wiki_grounding = FunctionTool(func=WGT.get_wiki_grounding)
search_grounding = FunctionTool(func=SGT.get_search_grounding)

finance_tools = [
    symbol_search, filter_symbols, symbol_name, symbol_quote,
    market_status, market_session, symbol_peers, local_datetime,
    last_market_close, all_exchange_codes, exchange_code, basic_financials,
    historical_candle, custom_candle, symbol_overview, symbol_trends,
    scored_news, wiki_grounding, search_grounding
]