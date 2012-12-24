import cmath # complex math library

def fftk(x, k):
  c = -1j * 2 * cmath.pi * k / len(x)
  Xk = 0
  for n, xn in enumerate(x):
    Xk += xn * cmath.exp(c * n)
  return Xk

X3 = fftk([1, 2, 0.1, -1.1, 5], 3)
