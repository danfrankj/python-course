import scipy.stats as stats

# generate two data samples from different distributions
samp1 = stats.norm.rvs(loc=0., scale=1., size=100)
samp2 = stats.norm.rvs(loc=2., scale=1., size=100)

# perform ks test: null hypothesis is distributions are the same
D, pval = stats.ks_2samp(samp1, samp2)  # D=.58, pval=1.34e-15

# reject the null


# generate two data samples from the same distribution
samp1 = stats.norm.rvs(loc=0., scale=1., size=100)
samp2 = stats.norm.rvs(loc=0., scale=1., size=100)

# perform ks test
D, pval = stats.ks_2samp(samp1, samp2)  # D=.09, pval=.79

# fail to reject the null
