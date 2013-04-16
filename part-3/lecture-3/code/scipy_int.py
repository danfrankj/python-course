# Example from:
# http://www.scipy.org/scipy_Example_List

# incorrect
from scipy import *

# correct
from scipy import integrate

value, err = integrate.quad(func=pow, a=0.,
                            b=1., args=(5,))
value  # integral of x^5 over [0,1]
