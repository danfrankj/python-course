import numpy as np
import scipy.linalg

X = np.array([[1, 2], [3, 4], [7, 8]])
y = [9, 12, 11]
Q, R = np.linalg.qr(X) # 1
z = np.dot(Q.T, y) # 2
betahat = scipy.linalg.solve_triangular(R, z) # 3
print betahat
