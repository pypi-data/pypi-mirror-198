import asyncio
from datetime import datetime, timedelta
from typing import Any, List, Sequence, Tuple

import pandas as pd
from pyalgotrader_protocols.symbol import Symbol_Protocol

from pyalgotrader_core.core import core
from pyalgotrader_core.data import Data


class DataManager:
    def __init__(
        self,
        symbol: Symbol_Protocol,
        timeframe: timedelta,
        range_from: str,
        range_to: str,
    ) -> None:
        self.name = symbol.name
        self.timeframe = timeframe
        self.range_from = range_from
        self.range_to = range_to

        self.fetch_from, self.fetch_to = self.__fetch_ranges()

        self.feed = core.broker.get_feed(self.name, timeframe)

        self.__columns = [
            "timestamp",
            "datetime",
            "symbol",
            "open",
            "high",
            "low",
            "close",
            "volume",
        ]

        self.__df: pd.DataFrame = self.__generate_dataframe([])

        self.__subscribers = []

    @property
    def df(self):
        return self.__df

    def add_subscriber(self, subscriber):
        self.__subscribers.append(subscriber)

    def __fetch_ranges(self) -> Tuple[int, int]:
        warmups_days = core.session.get_warmups_days(self.timeframe)

        warmups_from: str = str(
            (
                core.session.trading_days[
                    core.session.trading_days.index
                    < self.range_from.strftime("%Y-%m-%d")
                ]
                .tail(warmups_days)
                .head(1)
                .index[0]
            )
        )

        fetch_from_epoch = datetime.fromisoformat(warmups_from).replace(
            hour=core.session.market_start.hour,
            minute=core.session.market_start.minute,
            second=0,
            microsecond=0,
        )

        return int(fetch_from_epoch.timestamp()), int(core.session.range_to.timestamp())

    def __on_messages(self, messages: List[Data]) -> None:
        asyncio.run(self.on_ticks(messages))

    async def subscribe(self) -> None:
        try:
            loop = asyncio.get_running_loop()

            loop.run_in_executor(
                None, self.feed.subscribe, self.name, self.__on_messages
            )
        except KeyboardInterrupt:
            self.feed.unsubscribe(self.name)

            loop.close()

    async def run(self) -> None:
        if core.session.mode != "Backtest":
            await self.subscribe()

        await self.fetch_data()

    async def fetch_data(self) -> None:
        try:
            results = await self.feed.fetch_data(
                self.name,
                self.timeframe,
                self.fetch_from,
                self.fetch_to,
            )

            await self.on_bars(results)
        except Exception as e:
            print(e)

    async def on_bars(self, bars: List[Data]) -> None:
        try:
            items = [bar.get_item() for bar in bars]

            df = self.__generate_dataframe(items)

            self.__df = df.combine_first(self.__df)
        except Exception as e:
            print(e)

    async def on_ticks(self, ticks: List[Data]) -> None:
        try:
            items = [
                tick.convert_to_bar_time(core.session.market_start, self.timeframe)
                for tick in ticks
            ]

            df = self.__generate_dataframe(items)

            self.__df = df.combine_first(self.__df)

            await self.notify_subscribers_data(self.__df)
        except Exception as e:
            print(e)

    async def notify_subscribers_data(self, df):
        for subscriber in self.__subscribers:
            await subscriber.on_dataframe(df)

    def __generate_dataframe(self, data: Sequence[List[Any]]) -> pd.DataFrame:
        df = pd.DataFrame(data=data, columns=self.__columns)

        df.set_index(["datetime"], inplace=True)

        return df
