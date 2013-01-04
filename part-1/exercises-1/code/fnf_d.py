def func_d(x=0):
    if x < 0:
        return 'hello'
    elif x > 0:
        return 'world!'
    else:
        return ' '

print func_d(104) + func_d() + func_d(-11)
