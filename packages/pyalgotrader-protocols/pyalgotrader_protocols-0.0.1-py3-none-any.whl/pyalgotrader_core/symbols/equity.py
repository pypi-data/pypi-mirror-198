from pyalgotrader_core.core import core
from pyalgotrader_core.symbols.symbol import Symbol


class Equity(Symbol):
    segment = "Equity"

    def __init__(self, exchange, id, type, lot_size, strike_size):
        super().__init__(exchange, id, type, lot_size, strike_size)

        self.key = self.id
        self.name = core.broker.get_equity_name(self.segment, self.id)
