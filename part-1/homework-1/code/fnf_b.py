def func_b(x):
    if x < 0:
        return 'hello'
    elif x > 0:
        return 'world!'
    else:
        return ' '

print func_b(104) + func_b(0) + func_b(-11)
