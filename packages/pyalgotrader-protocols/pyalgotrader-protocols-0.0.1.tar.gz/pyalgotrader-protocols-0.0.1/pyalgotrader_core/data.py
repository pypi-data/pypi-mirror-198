from datetime import datetime, time, timedelta
from typing import Any, List


class Data:
    def __init__(
        self,
        tz,
        symbol: str,
        timestamp: int,
        open: float,
        high: float,
        low: float,
        close: float,
        volume: int,
    ) -> None:
        self.tz = tz
        self.timestamp = timestamp
        self.datetime = datetime.fromtimestamp(timestamp, tz=self.tz)
        self.symbol = symbol
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def get_item(self) -> List[Any]:
        return [
            self.timestamp,
            self.datetime,
            self.symbol,
            self.open,
            self.high,
            self.low,
            self.close,
            self.volume,
        ]

    def convert_to_bar_time(
        self, market_start: time, timeframe: timedelta
    ) -> List[Any]:
        try:
            market_start_datetime = datetime.now(tz=self.tz).replace(
                hour=market_start.hour,
                minute=market_start.minute,
                second=0,
                microsecond=0,
            )

            seconds, _ = divmod(
                (self.datetime - market_start_datetime).seconds,
                timeframe.total_seconds(),
            )

            self.datetime = market_start_datetime + timedelta(
                seconds=seconds * timeframe.total_seconds()
            )

            return self.get_item()
        except Exception as e:
            print("error", e)
