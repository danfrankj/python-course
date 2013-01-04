import cmath

def fftk(x, k=0, all=False):
    if all:
        return [fftk(x, k) for k in range(len(x))]
    c = -1j * 2 * cmath.pi * k / len(x)
    Xk = 0
    for n, xn in enumerate(x):
        Xk += xn * cmath.exp(c * n)
    return Xk

X = fftk([1, 2, 0.1, -1.1, 5], all=True)
