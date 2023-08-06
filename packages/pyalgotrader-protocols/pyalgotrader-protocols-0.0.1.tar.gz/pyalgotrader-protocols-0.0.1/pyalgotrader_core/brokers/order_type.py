from enum import Enum


class OrderType(Enum):
    LIMIT_ORDER = 1
    MARKET_ORDER = 2
    STOP_ORDER = 3
    STOP_LIMIT_ORDER = 4
