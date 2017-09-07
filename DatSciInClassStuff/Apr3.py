"""
kMeans clustering

A way to group data into logical clusters nd identify a prototype for each cluster

A data analysis trick - not a predictive trick

Algorithm is NP hard (brute force)

Uses random assignment and an evaluative function to determine how "good" the clustering and repeats, with movement
of the prototypes dependent on learning learning function

Algorithm:
1) Pick out k points (initial prototypes) in your data. k should represent the number of groups you are expecting
2) Group all remaining data into clusters based on the distance from the initial k points
3) Choose k new prototypes (these don't need to be data points) by taking the average of all elements in each cluster
4) Repeat until there are no changes to the prototypes
"""
from __future__ import print_function
from sklearn.cluster import KMeans
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import pairwise_distances_argmin

iris = datasets.load_iris()
print(type(iris))
dat_data = iris.data[:, 2:]
print(type(dat_data))
print(dat_data)

km = KMeans(n_clusters=3)
km.fit(dat_data)

centroids = km.cluster_centers_
dat_label = pairwise_distances_argmin(dat_data, centroids)
colors = ['b', 'c', 'r']

for k, col in zip(range(3), colors):
    mems = dat_label == k
    cent = centroids[k]
    plt.plot(dat_data[mems, 0], dat_data[mems, 1], 'w', markerfacecolor=col, marker='.')
    plt.plot(cent[0], cent[1], 'o', markerfacecolor=col, markersize=12)

plt.show()
