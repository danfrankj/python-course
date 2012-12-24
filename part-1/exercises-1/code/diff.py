def func():
    step = 1
    p1 = 2
    f1 = p1 ** 3 + 3 * p1 + 3
    p2 = p1 + step
    f2 = p2 ** 3 + 3 * p2 + 3
    return (f2 - f1) / step

fp2 = func()
print fp2
  
  
