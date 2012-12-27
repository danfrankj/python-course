def func_d(x=0):
    if x < 0:
        return 'hello'
    elif x > 0:
        return 'world!'
    else:
        return ' '

print func_b(104) + func_b() + func_b(-11)
