def func_c():
    i = 0
    j = 0
    while (i < 16):
        if i > 3:
            i += 2
        if i < 10:
            j += i
        else:
            j -= 1
        i += 1
    return j

print func_a()
