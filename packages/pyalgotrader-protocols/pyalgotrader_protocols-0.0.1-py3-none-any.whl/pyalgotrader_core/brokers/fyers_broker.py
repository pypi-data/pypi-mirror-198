from datetime import datetime, timedelta
from typing import Dict, List, Tuple

from fyers_api import accessToken, fyersModel
from fyers_api.Websocket import ws
from fyers_token_manager.main import FyersTokenManager
from pyalgotrader_core.brokers.fyers_feed import FyersFeed
from pyalgotrader_core.brokers.order import Order
from pyalgotrader_core.brokers.position import Position
from pyalgotrader_core.brokers.position_type import PositionType
from pyalgotrader_core.brokers.product_type import ProductType
from pyalgotrader_protocols.broker import Broker_Protocol
from pyalgotrader_protocols.feed import Feed_Protocol


class FyersBroker(Broker_Protocol):
    name = "Fyers"

    resolutions = {
        timedelta(minutes=1): "1",
        timedelta(minutes=3): "3",
        timedelta(minutes=5): "5",
        timedelta(minutes=15): "15",
        timedelta(minutes=30): "30",
        timedelta(hours=1): "60",
        timedelta(hours=2): "120",
        timedelta(hours=3): "180",
        timedelta(hours=4): "240",
        timedelta(days=1): "D",
    }

    __orders: List[Order] = []

    __positions: List[Position] = []

    __trades: List[Position] = []

    __symbols = {
        "NIFTY_BANK": {
            "Equity": "NSE:NIFTYBANK-INDEX",
            "Future": "NSE:BANKNIFTY",
            "Option": "NSE:BANKNIFTY",
        },
        "NIFTY_50": {
            "Equity": "NSE:NIFTY50-INDEX",
            "Future": "NSE:NIFTY",
            "Option": "NSE:NIFTY",
        },
        "INDIA_VIX": {
            "Equity": "NSE:INDIAVIX-INDEX",
            "Future": "NSE:INDIAVIX",
            "Option": "NSE:INDIAVIX",
        },
    }

    __leverage_multiplier = {
        ("equities", PositionType.BUY, ProductType.INTRADAY): 5,
        ("equities", PositionType.SELL, ProductType.INTRADAY): 5,
        ("futures", PositionType.BUY, ProductType.INTRADAY): 10,
        ("futures", PositionType.SELL, ProductType.INTRADAY): 10,
        ("futures", PositionType.BUY, ProductType.MARGIN): 10,
        ("futures", PositionType.SELL, ProductType.MARGIN): 10,
        ("options", PositionType.SELL, ProductType.INTRADAY): 10,
        ("options", PositionType.SELL, ProductType.MARGIN): 10,
    }

    def __init__(self, broker_config: Dict[str, str]) -> None:
        self.broker_config = broker_config

        self.token_manager = FyersTokenManager(
            config=broker_config, accessToken=accessToken, fyersModel=fyersModel, ws=ws
        )

        self.data_available_from = "2017-07-17"

        self.feeds: Dict[Tuple[str, datetime.timedelta], Feed_Protocol] = {}

    async def set_capital(self) -> None:
        self.__capital = 2_00_000

    @property
    def capital(self):
        return self.__capital

    async def get_margin(
        self, segment: str, position_type: PositionType, product_type: ProductType
    ) -> int:
        try:
            leverage_multiplier = self.__leverage_multiplier[
                (segment, position_type, product_type)
            ]

            leverage = (self.capital * leverage_multiplier) - self.capital
        except KeyError:
            leverage = 0

        return self.capital + leverage, leverage

    def get_feed(self, token: str, timeframe: timedelta) -> Feed_Protocol:
        key = (token, timeframe)

        try:
            return self.feeds[key]
        except KeyError:
            self.feeds[key] = FyersFeed(
                self.session.config.tz,
                self.resolutions,
                self.broker_config,
                self.token_manager,
                self.data_available_from,
            )

            return self.feeds[key]

    def get_orders(self) -> List[Order]:
        return self.__orders

    def get_positions(self) -> List[Position]:
        return self.__positions

    def get_trades(self) -> List[Position]:
        return self.__trades

    def get_leverages(self) -> Dict[Tuple[str, PositionType, ProductType], int]:
        return self.__leverage_multiplier

    def get_equity_name(self, segment: str, id: str) -> str:
        try:
            return self.__symbols[id][segment]
        except KeyError:
            raise Exception("Symbol not available")

    def get_future_name(self, segment: str, id: str, expiry: datetime) -> str:
        try:
            symbol_id = self.__symbols[id][segment]
            f_expiry: str = expiry.strftime("%y%^b")
            f_type = "FUT"

            return f"{symbol_id}{f_expiry}{f_type}"
        except KeyError:
            raise Exception("Symbol not available")

    def get_option_name(
        self,
        segment: str,
        id: str,
        expiry_period: str,
        expiry: datetime,
        strike_price: int,
        option_type: str,
    ) -> str:
        try:
            symbol_id = self.__symbols[id][segment]

            o_expiry: str = (
                expiry.strftime("%y%^b")
                if expiry_period == "monthly"
                else expiry.strftime("%y%-m%d")
            )

            return f"{symbol_id}{o_expiry}{strike_price}{option_type}"
        except KeyError:
            raise Exception("Symbol not available")
