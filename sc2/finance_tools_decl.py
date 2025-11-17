from google.adk.tools import FunctionTool

class FnTools:
    @classmethod
    def get_symbol_1(cls, q: str, exchange: str, query: str) -> dict:
        """Search for the stock ticker symbol of a given company, security, isin or cusip.

        Each ticker entry provides a description, symbol, and asset type.
        If this doesn't help you should try calling get_wiki_tool_response next.

        Args:
            q: The company, security, isin or cusip to search for a symbol.
            exchange: The exchange code used to filter results. When not specified the default exchange
                      code you should use is 'US' for the US exchanges. A dictionary mapping all supported
                      exchange codes to their names be retrieved by calling get_exchange_codes_1.
                      Search for an exchange code to use by calling get_exchange_code_1, specifying the
                      exchange code to search for.
            query: The question you're attempting to answer.

        Returns:
            A list of dictionaries, where each dictionary represents a ticker entry
            and typically contains 'description', 'symbol', and 'asset_type' keys.
            Example:
            [
            {
                "description": "Apple Inc.",
                "symbol": "AAPL",
                "asset_type": "Equity"
            },
            {
                "description": "Apple Hospitality REIT, Inc.",
                "symbol": "APLE",
                "asset_type": "Equity"
            }
            ]
        """
        pass # Function implementation would go here

    @classmethod
    def get_symbols_1(cls, exchange: str, query: str) -> list[dict]:
        """List all supported symbols and tickers, filtered by exchange code.

        Args:
            exchange: The exchange code used to filter the results.
            query: The question you're attempting to answer.

        Returns:
            A list of dictionaries, where each dictionary represents a supported symbol/ticker.
            Each dictionary typically contains keys like 'symbol', 'description', and 'asset_type'.
            Example:
            [
            {
                "symbol": "AAPL",
                "description": "Apple Inc.",
                "asset_type": "Equity"
            },
            {
                "symbol": "GOOG",
                "description": "Alphabet Inc. Class C",
                "asset_type": "Equity"
            }
            ]
        """
        pass # Function implementation would go here

    @classmethod
    def get_name_1(cls, q: str, exchange: str, query: str, company: str) -> list[dict]:
        """Search for the name associated with a stock ticker or symbol's company, security, isin or cusip.

        Each ticker entry provides a description, matching symbol, and asset type.

        Args:
            q: The symbol or ticker to search for.
            exchange: The exchange code used to filter results. When not specified the default exchange
                      code you should use is 'US' for the US exchanges. A dictionary mapping all supported
                      exchange codes to their names be retrieved by calling get_exchange_codes_1.
                      Search for an exchange code to use by calling get_exchange_code_1, specifying the
                      exchange code to search for.
            query: The question you're attempting to answer.
            company: The company you're searching for.

        Returns:
            A list of dictionaries, where each dictionary represents a ticker entry
            and typically contains 'description', 'symbol', and 'asset_type' keys.
            Example:
            [
            {
                "description": "Apple Inc.",
                "symbol": "AAPL",
                "asset_type": "Equity"
            },
            {
                "description": "Apple Hospitality REIT, Inc.",
                "symbol": "APLE",
                "asset_type": "Equity"
            }
            ]
        """
        pass # Function implementation would go here

    @classmethod
    def get_symbol_quote_1(cls, symbol: str, query: str, exchange: str) -> dict:
        """Search for the current price or quote of a stock ticker or symbol.

        The response is provided in JSON format. Each response contains the following key-value pairs:
        c: Current price,
        d: Change,
        dp: Percent change,
        h: High price of the day,
        l: Low price of the day,
        o: Open price of the day,
        pc: Previous close price,
        t: Epoch timestamp of price in seconds.

        Parse the response and respond according to this information.

        Args:
            symbol: The stock ticker symbol for a company, security, isin, or cusip.
            query: The question you're attempting to answer.
            exchange: The exchange code used to filter quotes. This must always be 'US'.

        Returns:
            A dictionary containing the current quote information for the specified symbol.
            Example:
            {
            "c": 170.00,
            "d": 1.50,
            "dp": 0.89,
            "h": 170.50,
            "l": 168.00,
            "o": 168.50,
            "pc": 168.50,
            "t": 1763362181 # Example timestamp
            }
        """
        pass # Function implementation would go here

    @classmethod
    def get_market_status_1(cls, exchange: str) -> dict:
        """Get the current market status of global exchanges.

        Includes whether exchanges are open or closed, and holiday details if applicable.
        The response is provided in JSON format. Each response contains the following key-value pairs:

        exchange: Exchange code,
        timezone: Timezone of the exchange,
        holiday: Holiday event name, or null if it's not a holiday,
        isOpen: Whether the market is open at the moment,
        t: Epoch timestamp of status in seconds (Eastern Time),
        session: The market session can be 1 of the following values:
                 pre-market, regular, post-market when open, or null if closed.

        Parse the response and respond according to this information.

        Args:
            exchange: The exchange code used to filter results. When not specified the default exchange
                      code you should use is 'US' for the US exchanges. A dictionary mapping all supported
                      exchange codes to their names be retrieved by calling get_exchange_codes_1.
                      Search for an exchange code to use by calling get_exchange_code_1, specifying the
                      exchange code to search for.

        Returns:
            A dictionary containing the market status for the specified exchange.
            Example:
            {
            "exchange": "US",
            "timezone": "America/New_York",
            "holiday": None,
            "isOpen": True,
            "t": 1763362181, # Example timestamp
            "session": "regular"
            }
            Or if closed/holiday:
            {
            "exchange": "US",
            "timezone": "America/New_York",
            "holiday": "New Year's Day",
            "isOpen": False,
            "t": 1763362181,
            "session": None
            }
        """
        pass # Function implementation would go here

    @classmethod
    def get_market_session_1(cls, exchange: str) -> str | None:
        """Get the current market session of global exchanges.

        Args:
            exchange: The exchange code used to filter results. When not specified the default exchange
                      code you should use is 'US' for the US exchanges. A dictionary mapping all supported
                      exchange codes to their names be retrieved by calling get_exchange_codes_1.
                      Search for an exchange code to use by calling get_exchange_code_1, specifying the
                      exchange code to search for.

        Returns:
            A string representing the current market session, which can be one of
            "pre-market", "regular", or "post-market" if the market is open.
            Returns `None` if the market is closed.
            Example: "regular"
            Example: "pre-market"
            Example: None
        """
        pass # Function implementation would go here

    @classmethod
    def get_company_peers_1(cls, symbol: str, grouping: str, exchange: str, query: str) -> dict:
        """Search for a company's peers.

        Returns a list of peers operating in the same country and in the same sector, industry, or subIndustry.
        Each response contains the following key-value pairs:
        symbol: The company's stock ticker symbol,
        peers: A list containing the peers.

        Each peers entry contains the following key-value pairs:
        symbol: The peer company's stock ticker symbol,
        name: The peer company's name.

        Parse the response and respond according to this information.

        Args:
            symbol: The stock ticker symbol of a company to obtain peers.
            grouping: This parameter may be one of the following values: sector, industry, subIndustry.
                      Always use subIndustry unless told otherwise.
            exchange: The exchange code used to filter results. When not specified the default exchange
                      code you should use is 'US' for the US exchanges. A dictionary mapping all supported
                      exchange codes to their names be retrieved by calling get_exchange_codes_1.
                      Search for an exchange code to use by calling get_exchange_code_1, specifying the
                      exchange code to search for.
            query: The question you're attempting to answer.

        Returns:
            A dictionary containing the symbol of the queried company and a list of its peers.
            Example:
            {
            "symbol": "AAPL",
            "peers": [
                {
                "symbol": "MSFT",
                "name": "Microsoft Corp."
                },
                {
                "symbol": "GOOGL",
                "name": "Alphabet Inc. Class A"
                }
            ]
            }
        """
        pass # Function implementation would go here

    @classmethod
    def get_local_datetime(cls, t: list[int]) -> list[str]:
        """Converts an array of timestamps from epoch time to the local timezone format.

        The result is an array of date and time in locale appropriate format.
        Suitable for use in a locale appropriate response.
        Treat this function as a vector function. Always prefer to batch timestamps for conversion.
        Use this function to format date and time in your responses.

        Args:
            t: An array of timestamps in seconds since epoch to be converted.
            The order of timestamps matches the order of conversion.

        Returns:
            A list of strings, where each string is a date and time in locale-appropriate format.
            Example:
            [
            "March 15, 2023 12:00:00 PM",
            "March 16, 2023 09:30:00 AM"
            ]
        """
        pass # Function implementation would go here

    @classmethod
    def get_last_market_close(cls, exchange: str) -> str:
        """Get the last market close of the specified exchange in Eastern Time.

        The response has already been converted by get_local_datetime, so this step should be skipped.

        Args:
            exchange: The exchange code used to filter results. When not specified the default exchange
                      code you should use is 'US' for the US exchanges. A dictionary mapping all supported
                      exchange codes to their names be retrieved by calling get_exchange_codes_1.
                      Search for an exchange code to use by calling get_exchange_code_1, specifying the
                      exchange code to search for.

        Returns:
            A string representing the date and time of the last market close in a locale-appropriate format.
            Example: "March 15, 2023 04:00:00 PM"
        """
        pass # Function implementation would go here

    @classmethod
    def get_exchange_codes_1(cls) -> dict[str, str]:
        """Get a dictionary mapping all supported exchange codes to their names.

        Returns:
            A dictionary where keys are exchange codes (strings) and values are exchange names (strings).
            Example:
            {
            "US": "US Exchanges",
            "LSE": "London Stock Exchange",
            "NYSE": "New York Stock Exchange"
            }
        """
        pass # Function implementation would go here

    @classmethod
    def get_exchange_code_1(cls, q: str) -> str:
        """Search for the exchange code to use when filtering by exchange.

        The result will be one or more exchange codes provided as a comma-separated string value.

        Args:
            q: Specifies which exchange code to search for.

        Returns:
            A comma-separated string of exchange codes.
            Example: "US"
            Example: "LSE,NYSE"
        """
        pass # Function implementation would go here

    @classmethod
    def get_financials_1(cls, symbol: str, metric: str, query: str) -> dict:
        """Get company basic financials such as margin, P/E ratio, 52-week high/low, etc.

        Parse the response for key-value pairs in JSON format and interpret their meaning as
        stock market financial indicators.

        Args:
            symbol: Stock ticker symbol for a company.
            metric: It must always be declared as the value 'all'.
            query: The question you're attempting to answer.

        Returns:
            A dictionary containing various financial indicators for the specified company.
            The exact keys and values will vary but typically include:
            Example:
            {
            "symbol": "AAPL",
            "margin": 0.25,
            "peRatio": 28.5,
            "52WeekHigh": 180.00,
            "52WeekLow": 120.00,
            "marketCap": 2800000000000,
            "eps": 6.11,
            "dividendYield": 0.005,
            # ... other financial metrics
            }
        """
        pass # Function implementation would go here

    @classmethod
    def get_daily_candlestick_2(cls, stocksTicker: str, date: str, adjusted: str, 
                                exchange: str, query: str) -> dict:
        """Get a daily stock ticker candlestick / aggregate bar (OHLC).

        Includes a day's open, high, low, and close prices.
        Also includes the day's trade volume and pre-market/after-hours trade prices.
        It provides the last trading day data after 11:59PM Eastern Time.

        Args:
            stocksTicker: The stock ticker symbol of a company to search for.
            date: The date of the requested candlestick in format YYYY-MM-DD.
            adjusted: May be 'true' or 'false'. Indicates if the results should be adjusted for splits.
                      Use 'true' unless told otherwise.
            exchange: The exchange code used to filter results. When not specified the default exchange
                      code you should use is 'US' for the US exchanges. A dictionary mapping all supported
                      exchange codes to their names be retrieved by calling get_exchange_codes_1.
                      Search for an exchange code to use by calling get_exchange_code_1, specifying the
                      exchange code to search for.
            query: The question you're attempting to answer.

        Returns:
            A dictionary containing the historical daily candlestick data for the specified date.
            A typical return value example:
            {
            "afterHours": 322.1,
            "close": 325.12,
            "from": "2023-01-09",
            "high": 326.2,
            "low": 322.3,
            "open": 324.66,
            "preMarket": 324.5,
            "status": "OK",
            "symbol": "AAPL",
            "volume": 26122646
            }
        """
        pass # Function implementation would go here

    @classmethod
    def get_custom_candlestick_2(cls, stocksTicker: str, multiplier: int, timespan: str,
                                 from_date: str,  # Renamed 'from' to 'from_date' to avoid Python keyword conflict
                                 to_date: str,    # Renamed 'to' to 'to_date' to avoid Python keyword conflict
                                 adjusted: str, sort: str, exchange: str, query: str) -> list[dict]:
        """Get a stock ticker candlestick / aggregate bar (OHLC) over a custom date range and time interval in Eastern Time.

        Includes open, high, low, and close prices. Also includes daily trade volume and 
        pre-market/after-hours trade prices. It includes the last trading days' data after 
        11:59PM Eastern Time.

        Args:
            stocksTicker: The stock ticker symbol of a company to search for.
            multiplier: The size of the timespan multiplier. For example, if the timespan is set to day,
                        and the multiplier is set to 2, then the results would be 2-day candlesticks.
            timespan: The size of the time window. This parameter may be one of the following values:
                      minute, hour, day, week, month, quarter, year. Always use day unless told otherwise.
            from_date: The start of the aggregate time window. Enter in YYYY-MM-DD format.
            to_date: The end of the aggregate time window. Enter in YYYY-MM-DD format.
            adjusted: May be 'true' or 'false'. Indicates if the results should be adjusted for splits.
                      Use 'true' unless told otherwise.
            sort: The order to sort the results by. This parameter may be one of the following values:
                  'asc' or 'desc'. Always use 'asc' unless told otherwise.
            exchange: The exchange code used to filter results. When not specified the default exchange
                      code you should use is 'US' for the US exchanges. A dictionary mapping all supported
                      exchange codes to their names be retrieved by calling get_exchange_codes_1.
                      Search for an exchange code to use by calling get_exchange_1, specifying the
                      exchange code to search for.
            query: The question you're attempting to answer.

        Returns:
            A list of dictionaries, where each dictionary represents a candlestick/aggregate bar
            for a specific time interval. A typical return value example:
            [
                {
                "c": Close price,
                "h": High price,
                "l": Low price,
                "n": Transaction count,
                "o": Open price,
                "t": Timestamp,
                "v": Volume,
                "vw": Volume weighted average price
                },
                ...
            ]
        """
        pass # Function implementation would go here

    @classmethod
    def get_ticker_overview_2(cls, ticker: str, query: str) -> dict:
        """Retrieve comprehensive details for a single ticker symbol.

        It's a deep look into a company’s fundamental attributes, including its primary exchange,
        standardized identifiers (CIK, composite FIGI, share class FIGI), market capitalization,
        industry classification, and key dates. Also includes branding assets in the form of icons and logos.

        Args:
            ticker: Stock ticker symbol of a company.
            query: The question you're attempting to answer.

        Returns:
            A dictionary containing comprehensive details about the ticker.
            Example:
            {
            "ticker": "AAPL",
            "name": "Apple Inc.",
            "primary_exchange": "NASDAQ",
            "cik": "0000320193",
            "composite_figi": "BBG000B9XRY4",
            "share_class_figi": "BBG001S5N8V8",
            "market_cap": 2800000000000,
            "locale": "us",
            "currency_name": "USD",
            "active": True,
            "market": "stocks",
            "phone_number": "1-408-996-1010",
            "description": "Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide.",
            "sic_code": "3674",
            "sic_description": "Semiconductors & Related Devices",
            "website": "https://www.apple.com",
            "address": {
                "address1": "One Apple Park Way",
                "city": "Cupertino",
                "state": "CA",
                "postal_code": "95014"
            },
            "branding": {
                "logo_url": "https://api.polygon.io/v1/reference/company-branding/AAPL/logo.png",
                "icon_url": "https://api.polygon.io/v1/reference/company-branding/AAPL/icon.png"
            },
            "share_class_shares_outstanding": 15720000000,
            "weighted_shares_outstanding": 15720000000,
            "round_lot": 100
            }
        """
        pass # Function implementation would go here

    @classmethod
    def get_recommendation_trends_1(cls, symbol: str, query: str) -> list[dict]:
        """Get the latest analyst recommendation trends for a company.

        The data includes the latest recommendations as well as historical
        recommendation data for each month. The data is classified according
        to these categories: strongBuy, buy, hold, sell, and strongSell.
        The date of a recommendation is indicated by the value of 'period'.

        Args:
            symbol: Stock ticker symbol for a company.
            query: The question you're attempting to answer.

        Returns:
            A list of dictionaries, where each dictionary represents the recommendation
            trends for a specific period. Each dictionary typically contains:
            'period': The date of the recommendation (e.g., "2023-03"),
            'strongBuy': Count of strong buy recommendations,
            'buy': Count of buy recommendations,
            'hold': Count of hold recommendations,
            'sell': Count of sell recommendations,
            'strongSell': Count of strong sell recommendations.
            Example:
            [
            {
                "period": "2023-03",
                "strongBuy": 10,
                "buy": 15,
                "hold": 5,
                "sell": 2,
                "strongSell": 0,
                "symbol": AAPL
            },
            {
                "period": "2023-02",
                "strongBuy": 9,
                "buy": 14,
                "hold": 6,
                "sell": 3,
                "strongSell": 1,
                "symbol": AAPL
            }
            ]
        """
        pass # Function implementation would go here

    @classmethod
    def get_news_with_sentiment_2(cls, limit: int, ticker: str, 
                                  published_utc_gte: str,  # Renamed from 'published_utc.gte' for valid Python argument name
                                  published_utc_lte: str,  # Renamed from 'published_utc.lte' for valid Python argument name
                                  order: str, sort: str, query: str) -> list[dict]:
        """Retrieve the most recent news articles related to a specified ticker.

        Each article includes comprehensive coverage, including a summary, publisher information,
        article metadata, and sentiment analysis.

        Args:
            limit: The number of results to return.
            ticker: Stock ticker symbol of a company.
            published_utc_gte: The start of the publication date range. Enter in YYYY-MM-DD format.
            published_utc_lte: The end of the publication date range. Enter in YYYY-MM-DD format.
            order: The order to sort the results by. This parameter may be one of the following values:
                   'asc' or 'desc'. Always use 'desc' unless told otherwise.
            sort: The field to sort the results by. This parameter may be one of the following values:
                  'published_utc', 'title', 'author'. Always use 'published_utc' unless told otherwise.
            query: The question you're attempting to answer.

        Returns:
            A list of dictionaries, where each dictionary represents a news article.
            A typical return value example:
            [
                {
                "amp_url": "https://m.uk.investing.com/news/stock-market-news/markets-are-underestimating-fed-cuts-ubs-3559968?ampMode=1",
                "article_url": "https://uk.investing.com/news/stock-market-news/markets-are-underestimating-fed-cuts-ubs-3559968",
                "author": "Sam Boughedda",
                "description": "UBS analysts warn that markets are underestimating the extent of future interest rate cuts by the Federal Reserve, as the weakening economy is likely to justify more cuts than currently anticipated.",
                "id": "8ec638777ca03b553ae516761c2a22ba2fdd2f37befae3ab6fdab74e9e5193eb",
                "image_url": "https://i-invdn-com.investing.com/news/LYNXNPEC4I0AL_L.jpg",
                "insights": [
                    {
                    "sentiment": "positive",
                    "sentiment_reasoning": "UBS analysts are providing a bullish outlook on the extent of future Federal Reserve rate cuts, suggesting that markets are underestimating the number of cuts that will occur.",
                    "ticker": "UBS"
                    }
                ],
                "keywords": [
                    "Federal Reserve",
                    "interest rates",
                    "economic data"
                ],
                "published_utc": "2024-06-24T18:33:53Z",
                "publisher": {
                    "favicon_url": "https://s3.massive.com/public/assets/news/favicons/investing.ico",
                    "homepage_url": "https://www.investing.com/",
                    "logo_url": "https://s3.massive.com/public/assets/news/logos/investing.png",
                    "name": "Investing.com"
                },
                "tickers": [
                    "UBS"
                ],
                "title": "Markets are underestimating Fed cuts: UBS By Investing.com - Investing.com UK"
                }
            ]
        """
        pass # Function implementation would go here

    @classmethod
    def get_wiki_grounding(cls, id: str, q: str) -> str:
        """Search for answers to a question using wikipedia.

        Retrieve a wiki page related to a company, product, or service.
        Each web page includes detailed company information, financial indicators,
        tickers, symbols, history, and products and services.

        Args:
            id: The question's company or product. Just the name and no other details.
            q: The full unaltered question string.

        Returns:
            A string containing the content of the wiki page, which includes detailed
            company information, financial indicators, tickers, symbols, history,
            and products and services.
            Example: "Apple Inc. (AAPL) is an American multinational technology company
                     headquartered in Cupertino, California. It designs, develops, and
                     sells consumer electronics, computer software, and online services.
                     Its products include the iPhone, iPad, Mac, Apple Watch, and Apple TV.
                     Key financial indicators include... (rest of the wiki page content)"
        """
        pass # Function implementation would go here

    @classmethod
    def get_search_grounding(cls, q: str, id: str) -> str:
        """Search for answers to a question using internet search.

        Retrieves internet search results related to a question.
        This information is less trustworthy than other sources.
        It can be used as a secondary source of answers.

        Args:
            q: The question needing an answer. Asked as a simple string.
            id: The question's company or product. In one word. Just the name and no other details.

        Returns:
            A string containing the answer to the question, retrieved from a general search.
            Example: "According to a recent search, the capital of France is Paris."
            Example: "The latest news indicates that the company 'Acme Corp' is developing new AI technology."
        """
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

finance_tools = [
    symbol_search, filter_symbols, symbol_name, symbol_quote,
    market_status, market_session, symbol_peers, local_datetime,
    last_market_close, all_exchange_codes, exchange_code, basic_financials,
    historical_candle, custom_candle, symbol_overview, symbol_trends,
    scored_news, wiki_grounding, search_grounding
]