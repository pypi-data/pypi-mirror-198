import asyncio
import datetime
import urllib.parse
from typing import Any, Callable, Dict, List

import httpx
from fyers_token_manager.main import FyersTokenManager
from pyalgotrader_core.data import Data
from pyalgotrader_core.helpers.generate_ranges import generate_ranges
from pyalgotrader_protocols.feed import Feed_Protocol


class FyersFeed(Feed_Protocol):
    def __init__(
        self,
        tz,
        resolutions: Dict[datetime.timedelta, str],
        broker_config: Dict[str, str],
        token_manager: FyersTokenManager,
        data_available_from: str,
    ) -> None:
        self.tz = tz
        self.resolutions = resolutions
        self.broker_config = broker_config
        self.token_manager = token_manager
        self.data_available_from = data_available_from

    def __format_message(self, message: Dict[str, Any]) -> Data:
        try:
            return Data(
                tz=self.tz,
                symbol=message["symbol"],
                timestamp=message["timestamp"],
                open=message["min_open_price"],
                high=message["min_high_price"],
                low=message["min_low_price"],
                close=message["min_close_price"],
                volume=message["min_volume"],
            )
        except Exception as e:
            raise e

    def __generate_url(
        self, symbol: str, timeframe: datetime.timedelta, fetch_from: int, fetch_to: int
    ) -> str:
        info = {
            "symbol": symbol,
            "resolution": self.resolutions[timeframe],
            "date_format": 0,
            "range_from": fetch_from,
            "range_to": fetch_to,
            "cont_flag": "1",
        }

        query_string = urllib.parse.urlencode(info)

        return "https://api.fyers.in/data-rest/v2/history/?" + query_string

    async def __fetch_data(
        self,
        client: httpx.AsyncClient,
        symbol: str,
        timeframe: datetime.timedelta,
        fetch_from: int,
        fetch_to: int,
    ) -> List[Data]:
        try:
            url = self.__generate_url(
                symbol,
                timeframe,
                fetch_from,
                fetch_to,
            )

            response = await client.get(
                url,
                headers={
                    "Authorization": f"{self.broker_config['client_id']}:{self.token_manager.http_access_token}"
                },
            )

            data = response.json()

            if data["s"] != "ok":
                raise Exception(response.json())

            return [
                Data(
                    tz=self.tz,
                    symbol=symbol,
                    timestamp=item[0],
                    open=item[1],
                    high=item[2],
                    low=item[3],
                    close=item[4],
                    volume=item[5],
                )
                for item in data["candles"]
            ]
        except Exception as e:
            raise e

    def subscribe(self, symbol: str, on_messages: Callable[[List[Data]], None]) -> None:
        try:
            self.token_manager.ws_client.websocket_data = lambda messages: on_messages(
                [self.__format_message(message) for message in messages]
            )

            self.token_manager.ws_client.subscribe(
                symbol=[symbol], data_type="symbolData"
            )

            self.token_manager.ws_client.keep_running()
        except Exception as e:
            raise e

    def unsubscribe(self, symbol: str) -> None:
        self.token_manager.ws_client.unsubscribe(symbol=[symbol])

    async def fetch_data(
        self, symbol: str, timeframe: datetime.timedelta, fetch_from: int, fetch_to: int
    ) -> List[Data]:
        try:
            ranges = generate_ranges(self.tz, fetch_from, fetch_to)

            limits = httpx.Limits(max_connections=5)

            async with httpx.AsyncClient(limits=limits) as client:
                tasks = [
                    self.__fetch_data(
                        client,
                        symbol,
                        timeframe,
                        range["fetch_from_epoch"],
                        range["fetch_to_epoch"],
                    )
                    for range in ranges
                ]

                results = await asyncio.gather(*tasks)

                return sum(results, [])
        except Exception as e:
            raise e
