import os
from datetime import datetime, time, timedelta
from typing import Dict

import pandas as pd
import pandas_market_calendars as mcal

from pyalgotrader_core.config import Config
from pyalgotrader_core.timeframes import timeframes


class Session:
    def __init__(self, session: Dict[str, str], config: Dict[str, str]) -> None:
        self.config = Config(config)

        self.now = datetime.now(tz=self.config.tz)
        self.market_start = time(9, 15)
        self.market_end = time(15, 30)
        self.market_status: str | None = None

        self.trading_days: pd.DataFrame = self.set_trading_days()
        self.expires: pd.DataFrame = self.set_expires()

        self.backtest_ranges: pd.DataFrame | None = None

        self.repository = session["repository"]
        self.mode = session["mode"]

        self.range_from = (
            self.get_range_from(session["range_from"])
            if self.mode == "Backtest"
            else self.now
        )

        self.range_to = (
            self.get_range_to(session["range_to"])
            if self.mode == "Backtest"
            else self.now
        )

        self.capital = session["capital"] if "capital" in session else 0

        if self.mode == "Backtest":
            if not self.range_from:
                raise Exception("range_from is required")

            if not self.range_to:
                raise Exception("range_to is required")

            if (self.range_to - self.range_from).days > 31:
                raise Exception("Backtest can be done within a month")

            self.backtest_ranges = self.trading_days[
                (
                    self.trading_days.index.strftime("%Y-%m-%d")
                    >= self.range_from.strftime("%Y-%m-%d")
                )
                & (
                    self.trading_days.index.strftime("%Y-%m-%d")
                    <= self.range_to.strftime("%Y-%m-%d")
                )
            ]

    def get_range_from(self, range_from):
        data = self.trading_days[self.trading_days.index >= range_from].head(1)
        return datetime.fromisoformat(data.index[0].strftime("%Y-%m-%d"))

    def get_range_to(self, range_to):
        data = self.trading_days[self.trading_days.index <= range_to].tail(1)
        return datetime.fromisoformat(data.index[0].strftime("%Y-%m-%d"))

    def set_trading_days(self) -> pd.DataFrame:
        current_directory = os.path.dirname(os.path.realpath(__file__))
        data_path = os.path.join(current_directory, "trading_days")
        file = f"{data_path}/{self.now.year}.csv"

        try:
            trading_days = pd.read_csv(
                file,
                index_col="datetime",
                parse_dates=["datetime", "market_open", "market_close"],
            )
        except FileNotFoundError:
            trading_days = self.__get_trading_days()

            trading_days.to_csv(
                file,
                columns=["market_open", "market_close", "weekly", "monthly"],
                index_label="datetime",
            )

        return trading_days

    def __get_trading_days(self) -> pd.DataFrame:
        nse = mcal.get_calendar("NSE")

        now = datetime.now(tz=self.config.tz)
        start_date = datetime(year=2017, month=7, day=17)
        end_date = datetime(year=now.year, month=12, day=31)

        trading_days: pd.DataFrame = nse.schedule(
            start_date=start_date, end_date=end_date, tz=self.config.tz
        )

        return trading_days

    def set_expires(self) -> pd.DataFrame:
        df_weekly_expires = self.trading_days.resample("W-THU").last()

        df_monthly_expires = df_weekly_expires[
            (df_weekly_expires.index + pd.offsets.Week(1)).month
            != df_weekly_expires.index.month
        ]

        return {"weekly": df_weekly_expires, "monthly": df_monthly_expires}

    def set_market_status(self, candle_open: datetime, timeframe: timedelta) -> None:
        candle_close = candle_open + timeframe

        if candle_close.time() >= self.market_end:
            self.market_status = "after_market_hours"

        elif candle_open.time() < self.market_start:
            self.market_status = "before_market_hours"

        else:
            self.market_status = "between_market_hours"

    def get_warmups_days(self, timeframe: timedelta) -> int:
        try:
            return timeframes[timeframe]
        except KeyError:
            raise Exception("Invalid timeframe")
