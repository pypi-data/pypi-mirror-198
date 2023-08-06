from abc import abstractmethod
from math import floor
from typing import List, Tuple

import pandas as pd
from pyalgotrader_protocols.chart import Chart_Protocol

from pyalgotrader_core.brokers.order import Order
from pyalgotrader_core.brokers.order_type import OrderType
from pyalgotrader_core.brokers.position import Position
from pyalgotrader_core.brokers.position_type import PositionType
from pyalgotrader_core.brokers.product_type import ProductType
from pyalgotrader_core.core import core
from pyalgotrader_core.loggers.orders_logger import OrdersLogger
from pyalgotrader_core.loggers.trades_logger import TradesLogger
from pyalgotrader_core.stoploss import FixedStoploss, TrailingStoploss
from pyalgotrader_core.store import Store
from pyalgotrader_core.symbol_list import SymbolList
from pyalgotrader_core.symbols.equity import Equity


class Algorithm(Store):
    __instance = None

    def __new__(cls) -> "Algorithm":
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self) -> None:
        super().__init__()

        self.symbols = SymbolList()

        self.BUY = PositionType.BUY
        self.SELL = PositionType.SELL

    @abstractmethod
    async def initialize(self) -> None:
        ...

    @abstractmethod
    async def get_candles(self) -> None:
        ...

    @abstractmethod
    async def next(self) -> None:
        ...

    @property
    def orders(self) -> List[Order]:
        return core.broker.get_orders()

    @property
    def positions(self) -> List[Position]:
        return core.broker.get_positions()

    @property
    def trades(self) -> List[Position]:
        return core.broker.get_trades()

    async def add_equity(self, symbol_info, timeframe):
        symbol = Equity(
            symbol_info["exchange"],
            symbol_info["id"],
            symbol_info["type"],
            symbol_info["lot_size"],
            symbol_info["strike_size"],
        )

        return await self.index_manager.register(symbol, timeframe)

    async def get_quantity(
        self,
        quantity: int | None,
        position_type: PositionType,
        product_type: ProductType,
        position: Position | None,
        chart: Chart_Protocol,
    ) -> Tuple[int, float]:
        data = await chart.get_data()

        lot_size = chart.symbol.lot_size
        price = data.close[-1]
        segment = chart.symbol.segment

        if position:
            if quantity:
                if quantity > position.quantity:
                    raise Exception(
                        "Quantity must be less that or equal to position Quantity"
                    )
                else:
                    return (quantity, 0)
            else:
                return (position.quantity, 0)
        else:
            margin, leverage = await core.broker.get_margin(
                segment, position_type, product_type
            )

            if quantity:
                if (quantity * price) > margin:
                    raise Exception(
                        "Quantity must be less that or equal to position Quantity"
                    )
                else:
                    return (quantity, leverage)
            else:
                size = margin / (price * lot_size)
                lot = int(floor(size))

                if lot == 0:
                    raise Exception(
                        f"Not enough margin, available: {round(margin, 2)}, required: {round((price * lot_size), 2)}"
                    )

                return (lot * lot_size, leverage)

    async def place_order(
        self,
        chart: Chart_Protocol,
        quantity: int | None,
        position_type: PositionType,
        product_type: ProductType,
        order_type: OrderType,
        limit_price: float | None,
        stop_price: float | None,
        sl: FixedStoploss | TrailingStoploss | None,
        tp: float | None,
        position: Position | None,
    ) -> None:
        try:
            if not chart.symbol.tradable:
                raise Exception("Symbol is not tradable")

            if order_type not in OrderType:
                raise Exception("Invalid order type")

            if order_type == OrderType.LIMIT_ORDER:
                if not limit_price:
                    raise Exception("Limit Price is required")

            if order_type == OrderType.STOP_LIMIT_ORDER:
                if not stop_price:
                    raise Exception("Stop Price is required")

                if not sl:
                    raise Exception("SL is required")

            if product_type == ProductType.BO:
                if not sl:
                    raise Exception("SL is required")

            if product_type == ProductType.CO:
                if not sl:
                    raise Exception("SL is required")

                if not tp:
                    raise Exception("TP is required")

            qty, leverage = await self.get_quantity(
                quantity, position_type, product_type, position, chart
            )

            await core.broker.place_order(
                chart,
                qty,
                leverage,
                position_type,
                product_type,
                order_type,
                limit_price,
                stop_price,
                sl,
                tp,
                position,
            )
        except Exception as e:
            print(e)

    async def buy(
        self,
        chart: Chart_Protocol,
        quantity: int | None = None,
        product_type: ProductType = ProductType.INTRADAY,
        order_type: OrderType = OrderType.MARKET_ORDER,
        limit_price: float | None = None,
        stop_price: float | None = None,
        sl: FixedStoploss | TrailingStoploss | None = None,
        tp: float | None = None,
    ) -> None:
        return await self.place_order(
            chart,
            quantity,
            PositionType.BUY,
            product_type,
            order_type,
            limit_price,
            stop_price,
            sl,
            tp,
            None,
        )

    async def sell(
        self,
        chart: Chart_Protocol,
        quantity: int | None = None,
        product_type: ProductType = ProductType.INTRADAY,
        order_type: OrderType = OrderType.MARKET_ORDER,
        limit_price: float | None = None,
        stop_price: float | None = None,
        sl: FixedStoploss | TrailingStoploss | None = None,
        tp: float | None = None,
    ) -> None:
        return await self.place_order(
            chart,
            quantity,
            PositionType.SELL,
            product_type,
            order_type,
            limit_price,
            stop_price,
            sl,
            tp,
            None,
        )

    async def exit(self, position: Position, quantity: int | None = None) -> None:
        quantity = quantity if quantity else position.quantity

        position_type = PositionType.SELL if position.is_buy else PositionType.BUY

        return await self.place_order(
            position.chart,
            quantity,
            position_type,
            position.product_type,
            OrderType.MARKET_ORDER,
            None,
            None,
            None,
            None,
            position,
        )

    async def run_logger(self) -> None:
        orders_logger = OrdersLogger(self.orders)
        trades_logger = TradesLogger(self.orders, self.trades, self.positions)

        await orders_logger.run()
        await trades_logger.run()
