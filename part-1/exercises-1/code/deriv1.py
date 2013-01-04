def func():
    step = 1
    point1 = 2
    point2 = point1 + step
    fp1 = point1 ** 3 + 3 * point1 + 3
    fp2 = point2 ** 3 + 3 * point2 + 3
    return (fp2 - fp1) / step

print func()
