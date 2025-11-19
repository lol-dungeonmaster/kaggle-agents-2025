import pytz
from datetime import datetime
from dateutil.parser import parse
from enum import Enum
from pydantic import BaseModel, field_validator
from typing import Optional
from api import Api

# Validation BaseModels in pydantic schema.
class RestStatus(Enum):
    OK = "OK"
    DELAY = "DELAYED"
    NONE = "NOT_FOUND"
    AUTH = "NOT_AUTHORIZED"

class StopGeneration(BaseModel):
    result: str = Api.Const.Stop()

class RestResultPoly(BaseModel):
    request_id: Optional[str] = None
    count: Optional[int] = None
    next_url: Optional[str] = None
    status: RestStatus  

class MarketSession(Enum):
    PRE = "pre-market"
    REG = "regular"
    POST = "post-market"
    CLOSED = "closed"
    NA = "not applicable"

class MarketEvent(Enum):
    PRE_OPEN = 0
    REG_OPEN = 1
    REG_CLOSE = 2
    POST_CLOSE = 3
    LAST_CLOSE = 4

class AssetClass(Enum):
    STOCKS = "stocks"
    OPTION = "options"
    CRYPTO = "crypto"
    FOREX = "fx"
    INDEX = "indices"
    OTC = "otc"

class SymbolType(Enum):
    COMMON = "Common Stock"
    ETP = "ETP"
    ADR = "ADR"
    REIT = "REIT"
    DELISTED = ""
    CEF = "Closed-End Fund"
    UNIT = "Unit"
    RIGHT = "Right"
    EQUITY = "Equity WRT"
    GDR = "GDR"
    PREF = "Preference"
    CDI = "CDI"
    NVDR = "NVDR"
    REG = "NY Reg Shrs"
    MLP = "MLP"
    MUTUAL = "Mutual Fund"

class Locale(Enum):
    US = "us"
    GLOBAL = "global"

class Sentiment(Enum):
    V_POS = "very positive"
    POSITIVE = "positive"
    NEUTRAL_P = "neutral/positive"
    NEUTRAL_SP = "neutral/slightly positive"
    NEUTRAL = "neutral"
    NEUTRAL_SN = "neutral/slightly negative"
    NEUTRAL_N = "neutral/negative"
    MIXED = "mixed"
    NEGATIVE = "negative"
    V_NEG = "very negative"

class Trend(Enum):
    S_BUY = "strong-buy"
    BUY = "buy"
    HOLD = "hold"
    SELL = "sell"
    S_SELL = "strong-sell"

class MarketCondition(Enum):
    BULL = "bullish"
    BULLN = "cautiously bullish"
    HOLD = "hold"
    BEARN = "cautiously bearish"
    BEAR = "bearish"

api = NewType("Api", None) # type: ignore (forward-decl)
class GeneratedEvent(BaseModel):
    last_close: str
    pre_open: str
    reg_open: str
    reg_close: str
    post_close: str
    timestamp: Optional[str] = None
    is_holiday: Optional[bool] = None

    def model_post_init(self, *args, **kwargs) -> None:
        if self.timestamp is None:
            self.timestamp = datetime.now(self.tz()).strftime('%c')
        if self.is_holiday is None:
            self.is_holiday = False

    def session(self, with_date: Optional[str] = None) -> MarketSession:
        if with_date is None:
            with_date = datetime.now(self.tz()).strftime('%c')
        compare = parse(with_date)
        if self.is_holiday or compare.weekday() > 4: # weekend
            return MarketSession.CLOSED
        events = [parse(event).time() for event in [self.pre_open,self.reg_open,self.reg_close,self.post_close]]
        if compare.time() < events[0]:
            return MarketSession.CLOSED
        else:
            session = MarketSession.NA
            if compare.time() >= events[0]:
                session = MarketSession.PRE
            if compare.time() >= events[1]:
                session = MarketSession.REG
            if compare.time() >= events[2]:
                session = MarketSession.POST
            if compare.time() >= events[3]:
                session = MarketSession.CLOSED
        return session

    def is_open(self) -> bool:
        return self.session() != MarketSession.CLOSED

    def has_update(self) -> bool:
        datetime_now = datetime.now(self.tz())
        self_ts = parse(self.timestamp)
        # Re-generate events for a new day.
        if datetime_now.day > self_ts.day:
            return True
        # No updates on holidays or when generated after post_close.
        if self.is_holiday or self_ts.time() >= parse(self.post_close).time():
            return False
        # Compare current time to generated event times.
        for event in [self.pre_open,self.reg_open,self.reg_close]:
            if datetime_now.time() > parse(event).time():
                return True
        # Current time is before pre_open.
        return False

    @classmethod
    def tz(cls):
        return pytz.timezone('US/Eastern') # Exchanges data is in eastern time.
    
    @classmethod
    def apply_fix(cls, value, fix: datetime) -> tuple[str, datetime]:
        api.validation_fail()
        value = fix.strftime('%c')
        return value, fix
    
    @field_validator("last_close")
    def valid_close(cls, value):
        date_gen = parse(value) # Generated close is in eastern time and tzinfo naive.
        date_now = parse(datetime.now(cls.tz()).strftime('%c')) # Need now in same format as generated.
        # Soft-pass: when actual session is closed after post-market
        if date_now.day == date_gen.day+1 and date_now.weekday() <= 4:
            date_fix = date_gen.replace(day=date_now.day)
            if date_fix.timestamp() < date_now.timestamp():
                value, date_gen = cls.apply_fix(value, date_fix) # soft-pass: use today's close
        # Soft-pass: when actual session is open post-market
        if date_now.day == date_gen.day and date_now.timestamp() < date_gen.timestamp():
            if date_now.weekday() > 0:
                date_fix = date_gen.replace(day=date_now.day-1)
            else:
                date_fix = date_gen.replace(day=date_now.day-3)
            if date_now.timestamp() > date_fix.timestamp():
                value, date_gen = cls.apply_fix(value, date_fix) # soft-pass: use previous close
        if date_now.weekday() == 0 or date_now.weekday() == 1 and date_gen.weekday() <= 4: # 0=monday, 4=friday
            return value # pass: generated thurs/friday on a monday/tues
        elif date_now.weekday() > 0 and date_now.weekday() <= 4 and date_gen.weekday() <= date_now.weekday()-1:
            return value # pass: generated yesterday/prior on a tues-fri
        elif date_now.weekday() > 4 and date_gen.weekday() <= 4:
            return value # pass: generated thurs/friday on a weekend
        elif date_now.day == date_gen.day and date_now.timestamp() > date_gen.timestamp():
            return value # pass: generated today after closed
        elif date_now.timestamp() < date_gen.timestamp():
            raise ValueError("last close cannot be a future value")
        else:
            raise ValueError("generated invalid last close")
        
class ChromaDBResult(BaseModel):
        docs: str
        dist: Optional[float] # requires query
        meta: Optional[dict]  # requires get or query
        store_id: str

class Aggregate(RestResultPoly):
    symbol: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    otc: Optional[bool] = None
    preMarket: Optional[float] = None
    afterHours: Optional[float] = None

class DailyCandle(Aggregate):
    from_date: str

class AggregateWindow(BaseModel):
    o: float
    h: float
    l: float
    c: float
    v: int # traded volume
    n: Optional[int] = None # transaction count
    vw: Optional[float] = None # volume weighted average price
    otc: Optional[bool] = None
    t: int

    @field_validator("t")
    def valid_t(cls, value):
        if not value > 0:
            raise ValueError("invalid timestamp")
        if len(str(value)) == 13:
            return int(value/1000)
        return value

class CustomCandle(RestResultPoly): 
    ticker: str
    adjusted: bool
    queryCount: int
    resultsCount: int
    results: list[AggregateWindow]

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[AggregateWindow]:
        return self.results
    
class MarketStatus(BaseModel):
    exchange: str
    holiday: Optional[str] = None
    isOpen: bool
    session: Optional[MarketSession] = None
    t: int
    timezone: str

    def model_post_init(self, *args, **kwargs) -> None:
        if self.session is None:
            self.session = MarketSession.CLOSED
        if self.holiday is None:
            self.holiday = MarketSession.NA.value

class MarketStatusResult(BaseModel):
    results: MarketStatus

    def get(self) -> MarketStatus:
        return self.results

class Symbol(BaseModel):
    description: str
    displaySymbol: str
    symbol: str
    type: SymbolType

class SymbolResult(BaseModel):
    count: int
    result: list[Symbol]

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.result)

    def get(self) -> list[Symbol]:
        return self.result

class Quote(BaseModel):
    c: float
    d: float
    dp: float
    h: float
    l: float
    o: float
    pc: float
    t: int

    @field_validator("t")
    def valid_t(cls, value):
        if not value > 0:
            raise ValueError("invalid timestamp")
        return value

class PeersResult(BaseModel):
    results: list[str]
    count: Optional[int] = None

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[str]:
        return self.results

class BasicFinancials(BaseModel):
    metric: dict
    metricType: str
    series: dict
    symbol: str

class Insight(BaseModel):
    sentiment: Sentiment|MarketCondition
    sentiment_reasoning: str
    ticker: str

class Publisher(BaseModel):
    favicon_url: Optional[str]
    homepage_url: str
    logo_url: str
    name: str

class NewsSummary(BaseModel):
    title: str
    summary: Optional[str]
    insights: Optional[list[Insight]]
    published_utc: str

class NewsTypePoly(BaseModel):
    amp_url: Optional[str] = None
    article_url: str
    title: str
    author: str
    description: Optional[str] = None
    id: str
    image_url: Optional[str] = None
    insights: Optional[list[Insight]] = None
    keywords: Optional[list[str]] = None
    published_utc: str
    publisher: Publisher
    tickers: list[str]

    def summary(self):
        return NewsSummary(title=self.title,
                           summary=self.description,
                           insights=self.insights,
                           published_utc=self.published_utc)

class NewsResultPoly(RestResultPoly):
    results: list[NewsTypePoly]

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[NewsTypePoly]:
        return self.results

class NewsTypeFinn(BaseModel):
    category: str
    datetime: int
    headline: str
    id: int
    image: str
    related: str # symbol
    source: str
    summary: str
    url: str

    def summary(self):
        return NewsSummary(title=self.headline,
                           summary=self.summary,
                           insights=None,
                           published_utc=self.datetime)

class NewsResultFinn(BaseModel):
    results: list[NewsTypeFinn]
    count: Optional[int] = None

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[NewsTypeFinn]:
        return self.results

class NewsTypeGenerated(BaseModel):
    title: str
    summary: str
    insights: list[Insight]
    keywords: list[str]
    source: Publisher
    published_utc: str
    tickers: list[str]
    url: str

    def summary(self):
        return NewsSummary(title=self.title,
                           summary=self.summary,
                           insights=self.insights,
                           published_utc=self.published_utc)

class TickerOverview(BaseModel):
    ticker: str
    name: str
    market: AssetClass
    locale: Locale
    primary_exchange: Optional[str] = None
    active: bool
    currency_name: str
    cik: Optional[str] = None
    composite_figi: Optional[str] = None
    share_class_figi: Optional[str] = None
    market_cap: Optional[int|float] = None
    phone_number: Optional[str] = None
    address: Optional[dict] = None
    description: Optional[str] = None
    sic_code: Optional[str] = None
    sic_description: Optional[str] = None
    ticker_root: Optional[str] = None
    homepage_url: Optional[str] = None
    total_employees: Optional[int] = None
    list_date: Optional[str] = None
    branding: Optional[dict] = None
    share_class_shares_outstanding: Optional[int] = None
    weighted_shares_outstanding: Optional[int] = None
    round_lot: Optional[int] = None

class OverviewResult(RestResultPoly):
    results: TickerOverview

    def get(self) -> TickerOverview:
        return self.results

class RecommendationTrend(BaseModel):
    buy: int
    hold: int
    period: str
    sell: int
    strongBuy: int
    strongSell: int
    symbol: str

class TrendsResult(BaseModel):
    results: list[RecommendationTrend]
    count: Optional[int] = None

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[RecommendationTrend]:
        return self.results