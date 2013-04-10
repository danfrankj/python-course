import numpy as np

A = np.ones(4)
A[0, 0] += 2
A12 = A[1, 2]

first_row = A[0,:]
last_col = A[:,-1]

