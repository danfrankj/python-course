import sklearn.datasets
import sklearn.cluster

# boston house price data features are
#   neighborhood statisticsm and target is 
#   median house value 
boston = sklearn.datasets.load_boston()
k_means = sklearn.cluster.KMeans(n_clusters=10)
k_means.fit(boston.data) 

# for each point, which cluster is it assigned?
k_means.labels_ 

# where is the center of each cluster?
k_means.cluster_centers_ 