def func_e(x=1, y=2):
    if x == y:
        return func_e(3, 0)
    return x - y

print func_e(5, 5) + func_e() + func_e(y=10, x=11)
