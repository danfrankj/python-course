def func_e(a, b):
    if a == b:
        return func_e(a - 1, b + 1)
    
    if a > b:
        def inner_func_e(x):
            if x < 0:
                return 10
            else:
                return 7
        return inner_func_e(a) + inner_func_e(b)

    return max(a, b)

print func_e(7, 7) + func_e(7, -7) + func_e(-7, 7)
