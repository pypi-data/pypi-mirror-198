from typing import Dict

import pytz


class Config:
    def __init__(self, config: Dict[str, str]) -> None:
        self.access_token = config["access_token"]
        self.backend_url = config["backend_url"]
        self.tz = pytz.timezone(config["tz"])
