import numpy as np

list_matrix = [[1, 3, 4], [2, 3, 5], [5, 7, 9]]
A = np.array(list_matrix)
b = np.array([4, 4, 4])

# Solve for Ax = b
x = np.linalg.solve(A, b)

