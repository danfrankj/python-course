A = np.ones(20, 5)
B = np.diag(np.arange(1, 6))
QA, QB, QC, RC = qr3(A, B)
print RC
