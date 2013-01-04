from stocks2 import *
class StockOption(Stock):
  def __init__(self, name, symbol,
               opt_price, date, prices=[]):
    Stock.__init__(self, name, symbol, prices)
    self.opt_price = opt_price
    self.date_available = date

fb_opt = StockOption('Facebook', 'FB', 24.56,
                     'Mar. 1, 2013', [19.56, 20.13])
print fb_opt.high_price()

