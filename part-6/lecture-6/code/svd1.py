import numpy as np
import matplotlib.pyplot as plt
A = np.random.randn(100, 100)
U, S, Vt = np.linalg.svd(A)
plt.plot(S)
plt.show()
