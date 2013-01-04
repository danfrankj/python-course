class Stock():
    def __init__(self, name, symbol, prices=[]):
        self.name = name
        self.symbol = symbol
        self.prices = prices

google = Stock('Google', 'GOOG')
apple = Stock('Apple', 'APPL', [500.43, 570.60])

print google.symbol
print str(max(apple.prices))
