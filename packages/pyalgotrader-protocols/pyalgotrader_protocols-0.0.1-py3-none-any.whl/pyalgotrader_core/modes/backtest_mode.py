from typing import Any, Dict

from pyalgotrader_protocols.broker import Broker_Protocol


class BacktestMode(Broker_Protocol):
    def __init__(self, config: Dict[str, Any]) -> None:
        super().__init__(config)
