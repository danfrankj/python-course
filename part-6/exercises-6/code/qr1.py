A = np.ones(20, 5)
B = np.diag(np.arange(1, 6))
Q, R = qr2(A, B)
print R
