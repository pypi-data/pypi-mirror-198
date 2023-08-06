from asyncio import sleep
from datetime import timedelta
from typing import Dict, List, Tuple

import pandas as pd
from pyalgotrader_protocols.chart import Chart_Protocol
from pyalgotrader_protocols.symbol import Symbol_Protocol

from pyalgotrader_core.chart import Chart
from pyalgotrader_core.core import core


class IndexManager:
    __instance = None

    def __new__(cls) -> "IndexManager":
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self) -> None:
        self.__timeframe: timedelta = timedelta(days=1)

        self.__charts: Dict[Tuple[str, timedelta], Chart_Protocol] = {}

        self.__datetime_index: pd.DatetimeIndex = core.session.range_from

    @property
    def charts(self) -> List[Chart_Protocol]:
        return [chart for chart in self.__charts.values()]

    @property
    def datetime_index(self):
        return self.__datetime_index

    def __set_timeframe(self, timeframe: timedelta) -> None:
        if timeframe < self.__timeframe:
            self.__timeframe = timeframe

    async def register(
        self, symbol: Symbol_Protocol, timeframe: timedelta
    ) -> Chart_Protocol:
        key = (symbol.key, timeframe)

        try:
            chart = self.__charts[key]
        except KeyError:
            chart = Chart(self, symbol, timeframe)

            self.__charts[key] = chart

            self.__set_timeframe(timeframe)

        return chart

    def datetime_generator(self):
        timeframe = self.__timeframe

        for _, series in core.session.backtest_ranges.iterrows():
            dt = series["market_open"]
            yield dt

            while (dt + timeframe) < series["market_close"]:
                dt += timeframe
                yield dt

    async def run_backtest(self, on_index):
        for dt_iterator in self.datetime_generator():
            self.__datetime_index = dt_iterator

            core.session.set_market_status(self.__datetime_index, self.__timeframe)

            for chart in self.charts:
                await chart.next()

            await on_index()

    async def run_live(self, on_index):
        while True:
            core.session.set_market_status(self.__datetime_index, self.__timeframe)

            if core.session.market_status == "between_market_hours":
                await sleep(1)

                for chart in self.charts:
                    await chart.next()

                await on_index()
