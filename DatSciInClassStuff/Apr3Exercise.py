from __future__ import print_function
import csv
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import pairwise_distances_argmin


all_data = []

with open("nyt1.csv") as csvfile1:
    reader1 = csv.reader(csvfile1)
    next(reader1, None)  # ignore first line of the csv file (header)
    all_data += list(reader1)

with open("nyt1.csv") as csvfile2:
    reader2 = csv.reader(csvfile2)
    next(reader2, None)  # ignore first line of the csv file (header)
    all_data += list(reader2)

for i in range(0, len(all_data)):
    for j in range(0, 5):
        all_data[i][j] = int(all_data[i][j])

print(all_data[0:4])

list2 = []

for k in range(0, len(all_data)):
    list2.append((all_data[k][0], all_data[k][1]))

np_data = np.asarray(list2)

print(type(np_data))
print(np_data[0:5])

km = KMeans(n_clusters=2)
km.fit(np_data)

centroids = km.cluster_centers_
dat_label = pairwise_distances_argmin(np_data, centroids)
colors = ['b', 'r']

for k, col in zip(range(2), colors):
    mems = dat_label == k
    cent = centroids[k]
    plt.plot(np_data[mems, 0], 'w', markerfacecolor=col, marker='.')
    plt.plot(cent[0], 'o', markerfacecolor=col, markersize=10)

plt.show()
