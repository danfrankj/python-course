import numpy as np

"""
weighted_sample(items, probs, N)

Return a weighted sample of size N with replacement from items
according to the probabilites specified in probs.

Hint: Use broadcasting and axis based operations and do NOT use
np.vectorize, map, np.apply_along_axis, etc. You may want to start
with np.cumsum()

Note: You can test your implementation by generating a large number
of samples and testing that the sampled frequency of the items
matches their probability.

Parameters
----------
items : np.array
    Any one dimensional array indexable by an integer np.array
probs : np.array
    An array of probabilities of the same size as items, probabilities
    must sum to one.
N : int, optional
    An integer number of samples. Default is 1.

Returns
-------
out : ndarray
    An one dimensional array object of size N containing
    the weighted samples.

Examples
--------
>>> probs = np.array([.4, .6])
>>> weighted_sample(np.array(['A', 'B'], probs, N=4))
array(['B', 'B', 'A', 'B'])
"""


# IMPLEMENT ME IN ONE LINE (the def line does not count, unlike last time)
def weighted_sample(items, probs, N=1):
    return items[np.zeros(N)]
