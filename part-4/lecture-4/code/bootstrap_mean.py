import numpy as np
import scipy.stats as stats

B = 1000
N = 100

# data array
arr = stats.norm.rvs(loc=np.pi, size=100)

# compute distribution of mean estimate
mean_distn = np.array([np.mean(arr[np.random.randint(N, size=N)])
                      for i in xrange(B)])

# 95% confidence interval [2.99, 3.39]
confidence_bounds = stats.mstats.mquantiles(mean_distn,
                                            prob=[.025, .975])
