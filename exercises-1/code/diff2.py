def diff(f, points, step=1):
    return [(f(p + step) - f(p)) / step for p in points]

print diff(lambda(x): x ** 3 + 3 * x + 3, [2, 3, 4, 5], 0.1)

  
  
