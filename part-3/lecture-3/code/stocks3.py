def Stock(name, symbol, prices=[]):
    def high_price(_self):
        if len(_self['prices']) is 0:
            return 'MISSING PRICES'
        return max(_self['prices'])
    s = {'name': name, 'symbol': symbol,
         'prices': prices}
    s['high_price'] = lambda(x): high_price(s)
    return s

apple = Stock('Apple', 'APPL', [500.43, 570.60])
print apple['high_price'](None)
