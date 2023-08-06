from typing import Any, Dict, List

from pyalgotrader_core.brokers.order import Order
from pyalgotrader_core.brokers.order_type import OrderType
from pyalgotrader_core.brokers.position import Position
from pyalgotrader_core.brokers.position_type import PositionType
from pyalgotrader_core.brokers.product_type import ProductType
from pyalgotrader_protocols.broker import Broker_Protocol


class PyalgotraderBroker(Broker_Protocol):
    name = "Pyalgotrader"

    __orders: List[Order] = []

    __positions: List[Position] = []

    __trades: List[Position] = []

    order_type = OrderType

    def __init__(self, broker_config: Dict[str, Any]) -> None:
        super().__init__(broker_config)

    async def set_capital(self) -> None:
        self.__capital = self.session.capital

    @property
    def capital(self):
        return self.__capital

    @property
    def market_closed(self) -> bool:
        return self.session.market_status == "after_market_hours"

    def get_orders(self) -> List[Order]:
        return self.__orders

    def get_positions(self) -> List[Position]:
        return self.__positions

    def get_trades(self) -> List[Position]:
        return self.__trades

    async def calculate_brokerage(self, leverage: float) -> float:
        flat_brokerage = 20

        leverage_brokerage = leverage * 0.00006

        charges = flat_brokerage + leverage_brokerage

        gst = charges * 0.18

        return charges + gst

    def get_position(self, order: Order) -> Position | None:
        positions = [
            position
            for position in self.__positions
            if (
                position.chart == order.chart
                and order.order_type == position.order_type
            )
        ]

        return positions[0] if len(positions) else None

    async def place_order(self, *args, **kwargs) -> None:
        try:
            order = Order(self, *args, **kwargs)

            self.__orders.append(order)

            await order.next(self.market_closed)
        except Exception as e:
            print(e)

    async def on_order(self, order: Order) -> None:
        if order.is_completed:
            position = self.get_position(order)

            if position:
                await self.exit_position(order, position)
            else:
                await self.enter_position(order)

    async def next(self) -> None:
        for position in self.__positions:
            await position.next(self.market_closed)

        for order in self.__orders:
            await order.next(self.market_closed)

    async def enter_position(self, order: Order) -> None:
        order_id = order.id
        chart = order.chart
        position_type = order.position_type
        product_type = order.product_type
        order_type = order.order_type
        quantity = order.quantity
        entry_price = order.price
        entry_date = order.date

        position = Position(
            self,
            order_id,
            chart,
            quantity,
            position_type,
            product_type,
            order_type,
            entry_price,
            entry_date,
        )

        self.__positions.append(position)

        await position.next(self.market_closed)

    async def exit_position(self, order: Order, position: Position) -> None:
        position.exit_price = order.price
        position.exit_date = order.date

        self.__trades.append(position)
        self.__positions = [item for item in self.__positions if item.id != position.id]
