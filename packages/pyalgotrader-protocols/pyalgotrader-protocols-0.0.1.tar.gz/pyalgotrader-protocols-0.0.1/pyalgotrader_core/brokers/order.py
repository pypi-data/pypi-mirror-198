import uuid
from datetime import datetime

from pyalgotrader_core.brokers.order_type import OrderType
from pyalgotrader_core.brokers.position import Position
from pyalgotrader_core.brokers.position_type import PositionType
from pyalgotrader_core.brokers.product_type import ProductType
from pyalgotrader_core.stoploss import FixedStoploss, TrailingStoploss
from pyalgotrader_protocols.broker import Broker_Protocol
from pyalgotrader_protocols.chart import Chart_Protocol


class Order:
    def __init__(
        self,
        broker: Broker_Protocol,
        chart: Chart_Protocol,
        quantity: int,
        leverage: float,
        position_type: PositionType,
        product_type: ProductType,
        order_type: OrderType,
        limit_price: float | None,
        stop_price: float | None,
        sl: FixedStoploss | TrailingStoploss | None,
        tp: float | None,
        position: Position | None,
    ) -> None:
        self.id = uuid.uuid4()
        self.broker = broker
        self.chart = chart
        self.quantity = quantity
        self.leverage = leverage
        self.position_type = position_type
        self.product_type = product_type
        self.order_type = order_type
        self.limit_price = limit_price
        self.stop_price = stop_price
        self.sl = sl
        self.tp = tp
        self.position = position

        self.price: float
        self.date: datetime

        self.brokerage: float

        self.status: str = "pending"

        if self.quantity and self.quantity % self.chart.symbol.lot_size != 0:
            raise Exception(
                f"Quantity must be in multiple of {self.chart.symbol.lot_size}"
            )

    async def next(self, market_closed: bool) -> None:
        if not self.is_pending:
            return

        if not self.position and market_closed:
            await self.cancelled()
        else:
            data = await self.chart.get_data()
            price = data.close[-1]
            date = datetime.fromtimestamp(
                data.timestamp[-1], self.broker.session.config.tz
            )

            self.price = price
            self.date = date

            self.brokerage = await self.broker.calculate_brokerage(self.leverage)

            await self.completed()

    @property
    def is_completed(self) -> bool:
        return self.status == "completed"

    @property
    def is_pending(self) -> bool:
        return self.status == "pending"

    async def pending(self) -> None:
        self.status = "pending"
        await self.broker.on_order(self)

    async def completed(self) -> None:
        self.status = "completed"
        await self.broker.on_order(self)

    async def cancelled(self) -> None:
        self.status = "cancelled"
        await self.broker.on_order(self)
