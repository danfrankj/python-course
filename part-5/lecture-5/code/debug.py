import numpy as np

def some_buggy_function():
    A = np.arange(1, 10)
    # import ipdb; ipdb.set_trace() # BREAKPOINT
    A /= 2.
    return np.sum(5 / A)