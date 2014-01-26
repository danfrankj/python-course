import numpy as np

v = [1, 2, 3]
w = [3, 2, 1]
A = np.vstack((v, w))

x = [4, 5, 7]
y = [1, 1, 0]
B = np.hstack((x, y))
print np.dot(A, B)
