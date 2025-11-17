from google.adk.tools import FunctionTool
from .finance_tools_def import FnTools

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

finance_tools = [
    symbol_search, filter_symbols, symbol_name, symbol_quote,
    market_status, market_session, symbol_peers, local_datetime,
    last_market_close, all_exchange_codes, exchange_code, basic_financials,
    historical_candle, custom_candle, symbol_overview, symbol_trends,
    scored_news, wiki_grounding, search_grounding
]