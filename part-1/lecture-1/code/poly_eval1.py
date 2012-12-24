def polyval(p, x):
    val = 0
    i = 0
    for coeff in p:
        val += coeff * (x ** i)  # ** is ^
        i = i + 1
    return val

print polyval([1, 2, 0, 1], 4)  # prints '73'
