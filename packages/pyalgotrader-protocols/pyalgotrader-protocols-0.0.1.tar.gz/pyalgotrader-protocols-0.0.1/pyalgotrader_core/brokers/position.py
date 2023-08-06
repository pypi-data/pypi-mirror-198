import uuid
from datetime import datetime

from pyalgotrader_core.brokers.order_type import OrderType
from pyalgotrader_core.brokers.position_type import PositionType
from pyalgotrader_core.brokers.product_type import ProductType
from pyalgotrader_protocols.broker import Broker_Protocol
from pyalgotrader_protocols.chart import Chart_Protocol


class Position:
    def __init__(
        self,
        broker: Broker_Protocol,
        order_id: uuid.UUID,
        chart: Chart_Protocol,
        quantity: int,
        position_type: PositionType,
        product_type: ProductType,
        order_type: OrderType,
        entry_price: float,
        entry_date: datetime,
    ) -> None:
        self.id = uuid.uuid4()
        self.broker = broker
        self.order_id = order_id
        self.chart = chart
        self.quantity = quantity
        self.position_type = position_type
        self.product_type = product_type
        self.order_type = order_type
        self.entry_price = entry_price
        self.entry_date = entry_date

        self.exit_price = None
        self.exit_date = None
        self.data = None

    @property
    def is_buy(self) -> bool:
        return self.position_type == PositionType.BUY

    async def next(self, market_closed):
        self.data = await self.chart.get_data()

        if market_closed:
            await self.square_off_position()

    async def square_off_position(self) -> None:
        if self.product_type == ProductType.INTRADAY:
            position_type = PositionType.SELL if self.is_buy else PositionType.BUY

            await self.broker.place_order(
                self.chart,
                self.quantity,
                0,
                position_type,
                self.product_type,
                OrderType.MARKET_ORDER,
                None,
                None,
                None,
                None,
                self,
            )

    @property
    def pnl(self) -> float:
        if not self.exit_price:
            exit_price = self.data.close[-1]
        else:
            exit_price = self.exit_price

        pnl: float = (
            exit_price - self.entry_price
            if self.position_type == PositionType.BUY
            else self.entry_price - exit_price
        )

        return round((pnl * self.quantity), 2)
