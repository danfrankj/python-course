def polyval(p, x):
    val = 0
    for i, coeff in enumerate(p):
        val += coeff * (x ** i)
    return val

print polyval([1, 2, 0, 1], 4)  # prints '73'
