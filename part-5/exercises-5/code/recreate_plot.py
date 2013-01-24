import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2. * np.pi, 20)
y = np.sin(x)

plt.plot(x, y, 'gx')
plt.xlim((0, 2. * np.pi))
plt.title('recreate me')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(label="some function")
plt.savefig('recreate_plot.png')
