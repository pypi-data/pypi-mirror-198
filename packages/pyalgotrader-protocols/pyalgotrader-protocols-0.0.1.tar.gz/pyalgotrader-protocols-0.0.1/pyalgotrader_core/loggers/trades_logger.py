from typing import List

import pandas as pd

from pyalgotrader_core.brokers.order import Order
from pyalgotrader_core.brokers.position import Position


class TradesLogger:
    def __init__(
        self, orders: List[Order], trades: List[Position], positions: List[Position]
    ) -> None:
        self.orders = orders
        self.trades = trades
        self.positions = positions

    async def run(self) -> None:
        columns = [
            "Symbol",
            "Quantity",
            "Entry Date",
            "Entry Price",
            "Exit Date",
            "Exit Price",
            "P&L",
        ]

        data = [
            [
                item.chart.symbol.name,
                item.quantity * item.position_type.value,
                item.entry_date,
                item.entry_price,
                item.exit_date,
                item.exit_price,
                item.pnl,
            ]
            for item in self.trades + self.positions
        ]

        df = pd.DataFrame(data=data, columns=columns)
        df.set_index("Symbol", inplace=True)

        if not len(df):
            print("No trades")
        else:
            gross_pnl = round(df["P&L"].sum(), 2)

            total_brokerage = round(
                sum([order.brokerage for order in self.orders if order.is_completed]), 2
            )

            net_pnl = round(gross_pnl - total_brokerage, 2)

            max_profit = df["P&L"].max()
            max_loss = df["P&L"].min()

            total_trades = len(df)
            winning_trades = len(df[df["P&L"] > 0])
            losing_trades = len(df[df["P&L"] < 0])
            accuracy = int((winning_trades / total_trades) * 100)

            print("\n")
            print(df)
            print("\n")
            print(f"Gross P&L Rs. {gross_pnl}")
            print(f"Brokerage Rs. {total_brokerage}")
            print(f"Net P&L Rs. {net_pnl}")
            print("\n")
            print(f"Maximum Profit Rs. {max_profit}")
            print(f"Maximum Loss Rs. {max_loss}")
            print("\n")
            print(f"Total Trades {total_trades}")
            print(f"Winning Trades {winning_trades}")
            print(f"Losing Trades {losing_trades}")
            print(f"Accuracy {accuracy}%")
