import numpy as np
import matplotlib.pyplot as plt

N = 2000
x = np.random.uniform(-1, 1, N)
y = np.random.uniform(-1, 1, N)
c = np.sqrt(x ** 2 + y ** 2)

plt.scatter(x, y, c=c, alpha=.3)
plt.xlim((-1, 1))
plt.ylim((-1, 1))
plt.savefig('rainbow_plot.png')
