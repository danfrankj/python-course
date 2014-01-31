import numpy as np

"""
better_kde(xvals, data, bw)

Return a the triangular kde evaluated at the points specified in
xvals.

Hint: Use broadcasting and axis based operations and do NOT use
np.vectorize, map, np.apply_along_axis, etc.

Parameters
----------
xvals : np.array
    One dimensional np.array of points to evaluate the kde
data : np.array
    One dimensional np.array of points .
bw : float or np.array
    An integer number of samples. Default is 1.

Returns
-------
out : np.array
    One dimensional np.array of the same size as xvals containing
    the evaluation of the kde at the points specified in xvals
"""


# IMPLEMENT ME IN ONE LINE (the def line does not count, unlike last time)
#   you should be able to modify your previous version of kde() slightly
#   to complete this question
def better_kde(xvals, data, bw):
    return np.zeros(xvals.size())


def plot_kde():
    import matplotlib.pyplot as plt
    N = 10
    data = np.random.exponential(size=N)
    # IMPLEMENT ME
    # insert code here to create a plot like the one included
    # with this assignment
    # i.e. create a single plot with two subplots, one with
    # bw = 1., and one with bw = 2. evaluating the kernel density
    # of the points given above as data
    plt.figure()

    # uncomment this line to show the plot
    # plt.show()

    plt.savefig('kde.png')
