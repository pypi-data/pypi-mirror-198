from dataclasses import dataclass


@dataclass
class Symbol:
    exchange: str
    id: str
    type: str
    lot_size: int
    strike_size: str

    @property
    def tradable(self) -> bool:
        return not (self.segment == "Equity" and self.type == "Index")
