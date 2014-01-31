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


def better_kde(xvals, data, bw):
    return np.mean(np.maximum(1. - np.abs(xvals - data[:, np.newaxis]) / bw, 0) / bw, axis=0)


def plot_kde():
    import matplotlib.pyplot as plt
    N = 10
    data = np.random.exponential(size=N)
    # insert code here to create a plot like the one included
    # with this assignment
    # i.e. create a single plot with two subplots, one with
    # bw = 1., and one with bw = 5. evaluating the kernel density
    # of the points given above as data
    grid = np.linspace(-1, np.max(data) + 1, 1000)
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.plot(grid, better_kde(grid, data, bw=1.), 'b-',
             data, np.zeros(data.size), 'kx')
    plt.title('bw = %s' % 1.)

    plt.subplot(1, 2, 2)
    plt.plot(grid, better_kde(grid, data, bw=5.), 'g-',
             data, np.zeros(data.size), 'kx')
    plt.title('bw = %s' % 5.)

    plt.savefig('kde.png')
    # uncomment this line to show the plot
    plt.show()


