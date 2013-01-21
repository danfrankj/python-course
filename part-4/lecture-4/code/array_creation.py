import numpy as np

#  lists
arr = np.array([[1, 2, 3], [4, 5, 6]])

#In [1]: arr
#Out[1]:
#array([[1, 2, 3],
#       [4, 5, 6]])

#  sequences
np.arange(0, 10, 0.1)
np.linspace(0, 2 * np.pi, 100)

#  zeros & ones
np.zeros((5, 5))
np.ones((5, 5))

#  random
np.random.random(size=(3, 4))
np.random.normal(loc=10., scale=3., size=(3, 4, 5))
