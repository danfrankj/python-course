import numpy as np

x = np.array([2, 2])
y = [2, 2]
A = np.array([[1, 2], [1, 2]])
print np.dot(A, x), np.dot(A, y)
print np.dot(x, A), np.dot(y, A)

