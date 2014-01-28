import numpy as np
import matplotlib.pyplot as plt
A = np.random.randn(100, 50)
B = np.hstack((A, A))
U, S, Vt = np.linalg.svd(B)
plt.plot(S)
plt.show()
