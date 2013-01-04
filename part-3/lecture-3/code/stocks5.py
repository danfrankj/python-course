from stocks2 import *
class StockOption(Stock):
  def __init__(self, name, symbol,
               opt_price, date, prices=[]):
    Stock.__init__(self, name, symbol, prices)
    self.opt_price = opt_price
    self.date_available = date

  def high_price(self):
    if len(self.prices) is 0:
      return self.opt_price
    return max(self.opt_price, max(self.prices))
