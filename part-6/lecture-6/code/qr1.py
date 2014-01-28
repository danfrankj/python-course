import numpy as np

X = np.array([[1, 2], [3, 4], [7, 8]])
y = [9, 12, 11]
Q, R = np.linalg.qr(X) # 1
z = np.dot(Q.T, y) # 2
betahat = np.linalg.solve(R, z) # 3
print betahat
