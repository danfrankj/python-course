from stocks2 import *
class Portfolio():
  def __init__(self):
    google = Stock('Google', 'GOOG')
    facebook = Stock('Facebook', 'FB', [19.56])
    self.stocks = [google, facebook]

  def __contains__(self, key):
    for s in self.stocks:
      if key in [s.symbol, s.name]: return True
    return False

portfolio = Portfolio()
if 'FB' in portfolio: print 'I own Facebook stock!'
