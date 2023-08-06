from typing import Callable

import pandas as pd


class Indicator:
    def __init__(self, chart, fn: Callable[[pd.DataFrame], pd.DataFrame]) -> None:
        self.chart = chart
        self.fn = fn

        self.__df: pd.DataFrame = pd.DataFrame()

    async def get_data(self) -> pd.DataFrame:
        if self.__df.empty:
            data_manager = await self.chart.get_data_manager()
            await self.on_dataframe(data_manager.df)

        return self.__df[self.__df.index <= self.chart.index_manager.datetime_index]

    async def on_dataframe(self, df) -> None:
        indicator_data = self.fn(df)

        if isinstance(indicator_data, pd.DataFrame):
            self.__df = indicator_data
        elif isinstance(indicator_data, pd.Series):
            self.__df = pd.DataFrame(data=indicator_data)
        else:
            raise Exception("add more warmups days")
