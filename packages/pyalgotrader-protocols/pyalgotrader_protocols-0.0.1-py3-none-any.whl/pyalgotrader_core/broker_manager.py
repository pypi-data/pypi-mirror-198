from typing import Dict, Type

from pyalgotrader_core.brokers.fyers_broker import FyersBroker
from pyalgotrader_core.brokers.pyalgotrader_broker import PyalgotraderBroker
from pyalgotrader_core.modes.backtest_mode import BacktestMode
from pyalgotrader_core.modes.live_mode import LiveMode
from pyalgotrader_core.modes.paper_mode import PaperMode
from pyalgotrader_protocols.broker import Broker_Protocol


class BrokerManager:
    available_brokers = ["Fyers"]

    available_modes = ["Backtest", "Paper", "Live"]

    modes: Dict[str, Type[Broker_Protocol]] = {
        "Backtest": BacktestMode,
        "Paper": PaperMode,
        "Live": LiveMode,
    }

    brokers: Dict[str, Type[Broker_Protocol]] = {
        "Fyers": FyersBroker,
    }

    __instance = None

    def __new__(
        cls, mode: str, broker_name: str, broker_config: Dict[str, str]
    ) -> "BrokerManager":
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(
        self, mode: str, broker_name: str, broker_config: Dict[str, str]
    ) -> None:
        self.mode = mode
        self.broker_name = broker_name
        self.broker_config = broker_config

    def get_broker(self) -> "Broker_Protocol":
        try:
            main_broker = self.brokers[self.broker_name]

            broker_class = None

            if self.mode == "Live":
                broker_class = main_broker
            else:
                PyalgotraderBroker.__bases__ = (self.brokers[self.broker_name],)

                broker_class = PyalgotraderBroker

            mode_class = self.modes[self.mode]

            mode_class.__bases__ = (broker_class,)

            return mode_class(self.broker_config)
        except IndexError:
            raise Exception("Unknown broker")
