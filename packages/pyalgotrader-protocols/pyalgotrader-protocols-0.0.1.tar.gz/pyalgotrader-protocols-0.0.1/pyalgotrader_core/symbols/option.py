from pyalgotrader_core.core import core
from pyalgotrader_core.symbols.symbol import Symbol


class Option(Symbol):
    segment = "Option"

    def __init__(
        self,
        exchange,
        id,
        type,
        lot_size,
        strike_size,
        expiry_period,
        expiry,
        strike_price,
        option_type,
    ):
        super().__init__(exchange, id, type, lot_size, strike_size)

        self.expiry_period = expiry_period
        self.expiry = expiry
        self.strike_price = strike_price
        self.option_type = option_type

        self.key = (self.id, self.expiry, self.strike_price, self.option_type)
        self.name = core.broker.get_option_name(
            self.segment,
            self.id,
            self.expiry_period,
            self.expiry,
            self.strike_price,
            self.option_type,
        )
