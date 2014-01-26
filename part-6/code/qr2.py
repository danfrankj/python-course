import numpy as np

A = np.array([[1, 2], [3, 4], [7, 8]])
y = [9, 12, 11]

'''
Q, R = np.linalg.qr(A)
z = np.dot(Q.T, y)
betahat = np.linalg.solve(R, z)
'''

betahat = np.linalg.lstsq(A, y)[0]
print betahat
