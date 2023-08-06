from typing import List

import pandas as pd

from pyalgotrader_core.brokers.order import Order


class OrdersLogger:
    def __init__(self, orders: List[Order]) -> None:
        self.orders = orders

    async def run(self) -> None:
        columns = [
            "Symbol",
            "Date",
            "Price",
            "Quantity",
            "Brokerage",
        ]

        data = [
            [
                item.chart.symbol.name,
                item.date,
                item.price,
                item.quantity * item.position_type.value,
                item.brokerage,
            ]
            for item in self.orders
            if item.status == "completed"
        ]

        df = pd.DataFrame(data=data, columns=columns)
        df.set_index("Symbol", inplace=True)

        print("\n")
        print(df)
        print("\n")
