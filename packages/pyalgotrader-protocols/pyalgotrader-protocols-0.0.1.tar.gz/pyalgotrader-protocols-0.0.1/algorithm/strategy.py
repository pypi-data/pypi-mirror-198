from datetime import timedelta

import pandas_ta as ta
from pyalgotrader_protocols.strategy import Strategy_Protocol


class Strategy(Strategy_Protocol):
    async def initialize(self) -> None:
        self.nifty_bank = await self.add_equity(
            self.symbols.NIFTY_BANK, timedelta(minutes=5)
        )

        await self.nifty_bank.set_option_filter(self.set_nifty_bank_options)

    async def set_nifty_bank_options(self) -> None:
        option_provider = self.nifty_bank.option_provider

        self.nifty_bank_ce = await option_provider.add_option(("weekly", 0), -2, "CE")
        self.nifty_bank_pe = await option_provider.add_option(("weekly", 0), +2, "PE")

    @property
    def macd(self):
        return self.nifty_bank.add_indicator(
            "macd", lambda data: ta.macd(data.close, 12, 26, 9)
        )

    @property
    def rsi_14(self):
        return self.nifty_bank.add_indicator(
            "rsi_14", lambda data: ta.rsi(data.close, 14)
        )

    @property
    def adx_14(self):
        return self.nifty_bank.add_indicator(
            "adx_14", lambda data: ta.adx(data.high, data.low, data.close, 14)
        )

    async def next(self) -> None:
        print("test")

        # rsi_14_data = await self.rsi_14.get_data()
        # adx_14_data = await self.adx_14.get_data()
        # macd_data = await self.macd.get_data()

        # macd_signal = (
        #     "long"
        #     if macd_data["MACD_12_26_9"][-2] > macd_data["MACDs_12_26_9"][-2]
        #     else "short"
        # )

        # rsi_signal = rsi_14_data["RSI_14"][-2] > 30 and rsi_14_data["RSI_14"][-2] < 70

        # adx_signal = (
        #     adx_14_data["ADX_14"][-2] > 20
        #     and adx_14_data["ADX_14"][-1] > adx_14_data["ADX_14"][-2]
        # )

        # if not self.positions:
        #     should_long = macd_signal == "long" and rsi_signal and adx_signal
        #     should_short = macd_signal == "short" and rsi_signal and adx_signal

        #     if should_long:
        #         await self.buy(self.nifty_bank_ce)
        #     if should_short:
        #         await self.buy(self.nifty_bank_pe)
        # else:
        #     for position in self.positions:
        #         if position.pnl <= (position.quantity * -20):
        #             await self.exit(position)

        #         if position.pnl >= (position.quantity * +40):
        #             await self.exit(position)
