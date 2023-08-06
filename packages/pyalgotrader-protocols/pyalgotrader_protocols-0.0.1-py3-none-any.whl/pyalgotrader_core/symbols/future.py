from pyalgotrader_core.core import core
from pyalgotrader_core.symbols.symbol import Symbol


class Future(Symbol):
    segment = "Future"

    def __init__(self, exchange, id, type, lot_size, strike_size, expiry):
        super().__init__(exchange, id, type, lot_size, strike_size)

        self.expiry = expiry

        self.key = (self.id, self.expiry)
        self.name = core.broker.get_future_name(self.segment, self.id, self.expiry)
