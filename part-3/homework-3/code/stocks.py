class Portfolio():
  def __init__(self):
    self.stocks = {}

  """
   Add the number of shares to the stock in this portfolio.
   At this moment, price_per_share is the price of the stock,
   so update the price per share of the stock in your Portfolio
   if you already own the stock
  """
  def add_stock(self, symbol, price_per_share, shares):
    # IMPLEMENT
    return

  """
   Return the symbol of the stock in which this portfolio
   is the most invested.  In other words, return the symbol
   of the stock for which the price per share multiplied by the
   number of shares is the most.
  """
  def most_money(self):
    # IMPLEMENT
    return ''

  """
   Implement __contains__ so that it returns True if the stock symbol
   (provided by key) is in this portfolio.
  """
  def __contains__(self, key):
    # IMPLEMENT
    return False

techs = Portfolio()

def test1():
  techs.add_stock('APPL', 600.41, 0.3)
  techs.add_stock('GOOG', 630.29, 1.2)
  techs.add_stock('FB', 19.56, 30)
  print techs.most_money()
  # Facebook just skyrocketed!
  techs.add_stock('FB', 45.73, 2)
  print techs.most_money()

def test2():
  if 'P' not in techs:
    print 'Maybe I should buy Pandora stock'
    techs.add_stock('P', 18.73, 70)
  if 'P' in techs:
    print 'I now have Pandora stock'


if __name__ == '__main__':
  print 'running test 1...'
  test1()
  print 'running test 2...'
  test2()
