import numpy as np

"""
weighted_sample(items, probs, N)

Return a weighted sample of size N with replacement from items
according to the probabilites specified in probs. Code uses both
broadcasting and axis based operation.

Slight inefficiency in using np.argmax but finding the first
true value is still a requested feature
https://github.com/numpy/numpy/issues/2269,
not that it'd be too hard to write it ourselves.

Parameters
----------
items : np.array
    Any one dimensional array indexable by an integer np.array
probs : np.array
    An array of probabilities of the same size as items, probabilities
    must sum to one.
N : int, optional
    An integer number of samples. Default is 1.
"""

def weighted_sample(items, probs, N=1):
    cumprobs = np.concatenate((np.zeros(1), np.cumsum(probs)))
    return items[np.argmax(np.random.random(size=N) <
                           cumprobs[:, np.newaxis], axis=0) - 1]
