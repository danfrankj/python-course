import numpy as np
import matplotlib.pyplot as plt

A = np.random.random((100, 100))
plt.imshow(A)
plt.hot()
plt.colorbar()

plt.savefig('imageplot.png')
