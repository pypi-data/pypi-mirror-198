from pyalgotrader_core.core import core
from pyalgotrader_core.data_manager import DataManager
from pyalgotrader_core.indicator import Indicator
from pyalgotrader_core.providers.future_provider import FutureProvider
from pyalgotrader_core.providers.option_provider import OptionProvider


class Chart:
    def __init__(self, index_manager, symbol, timeframe) -> None:
        self.index_manager = index_manager
        self.symbol = symbol
        self.timeframe = timeframe

        self.data_manager = None
        self.__indicators = {}

        self.__filters = []

        self.future_provider = FutureProvider(self)
        self.option_provider = OptionProvider(self)

    async def next(self):
        for filter in self.__filters:
            await filter["value"]()

    @property
    def indicators(self):
        return [indicator for indicator in self.__indicators.values()]

    async def get_data(self):
        data_manager = await self.get_data_manager()

        return data_manager.df[
            data_manager.df.index <= self.index_manager.datetime_index
        ]

    async def get_data_manager(self):
        if not self.data_manager:
            self.data_manager = DataManager(
                self.symbol,
                self.timeframe,
                core.session.range_from,
                core.session.range_to,
            )

            self.data_manager.add_subscriber(self)

            await self.data_manager.run()

            return self.data_manager
        else:
            return self.data_manager

    async def on_dataframe(self, df):
        for indicator in self.indicators:
            await indicator.on_dataframe(df)

    def add_indicator(self, key, indicator_fn):
        try:
            return self.__indicators[key]
        except KeyError:
            indicator = Indicator(self, indicator_fn)

            self.__indicators[key] = indicator

            return indicator

    async def set_future_filter(self, future_filter):
        self.__filters.append({"key": "future", "value": future_filter})

    async def set_option_filter(self, option_filter):
        self.__filters.append({"key": "option", "value": option_filter})
