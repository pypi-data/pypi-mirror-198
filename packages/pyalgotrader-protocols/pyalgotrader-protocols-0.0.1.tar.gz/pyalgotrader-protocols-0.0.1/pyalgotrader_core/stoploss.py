from dataclasses import dataclass
from typing import Any, Callable, Optional


@dataclass
class BaseStoploss:
    stoploss: float


@dataclass
class FixedStoploss(BaseStoploss):
    pass


@dataclass
class TrailingStoploss(BaseStoploss):
    trail_by: Optional[float]
    trail_when: Optional[Callable[[Any], bool]]
