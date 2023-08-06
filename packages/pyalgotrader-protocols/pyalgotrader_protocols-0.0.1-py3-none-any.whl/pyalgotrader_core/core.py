from sys import argv
from typing import Any, Dict, List

import jwt

from pyalgotrader_core.broker_manager import BrokerManager
from pyalgotrader_core.session import Session


class Core:
    __instance = None

    def __new__(cls) -> "Core":
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self) -> None:
        self.validate_session_info()

    def get_session_info(self, key: str, data: List[str]) -> Dict[str, Any]:
        filtered_key = f"--{key}="

        items = [
            item.replace(filtered_key, "") for item in data if filtered_key in item
        ]

        if len(items):
            return jwt.decode(items[0], "secret", algorithms=["HS256"])
        else:
            raise Exception("Invalid session data")

    def validate_session_info(self) -> None:
        data = self.get_session_info("data", argv)

        config = data["config"]
        session = data["session"]
        broker_name = data["broker"]["name"]
        broker_config = data["broker"]["config"]

        self.session = Session(session, config)

        self.broker_manager = BrokerManager(
            self.session.mode, broker_name, broker_config
        )

        broker = self.broker_manager.get_broker()
        broker.__setattr__("session", self.session)
        self.broker = broker


core = Core()
