import datetime
from abc import ABC, abstractmethod

from pyalgotrader_protocols.symbol import Symbol_Protocol

from pyalgotrader_core.brokers.order_type import OrderType
from pyalgotrader_core.chart import Chart
from pyalgotrader_core.core import core
from pyalgotrader_core.index_manager import IndexManager
from pyalgotrader_core.stoploss import FixedStoploss, TrailingStoploss


class Store(ABC):
    order_type = OrderType

    fixed_stoploss = FixedStoploss

    trailing_stoploss = TrailingStoploss

    def __init__(self) -> None:
        self.index_manager = IndexManager()

    @abstractmethod
    async def add_equity(
        self, symbol: Symbol_Protocol, timeframe: datetime.timedelta
    ) -> Chart:
        pass

    async def boot(self) -> None:
        await core.broker.set_capital()

        await self.initialize()

    async def run(self) -> None:
        try:
            if core.session.mode == "Backtest":
                await self.index_manager.run_backtest(self.on_index)
            else:
                await self.index_manager.run_live(self.on_index)

            await self.run_logger()
        except Exception as e:
            raise e

    async def on_index(self) -> None:
        try:
            await core.broker.next()
            await self.next()
        except Exception as e:
            raise e
