from __future__ import print_function
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
"""
k-nearest neighbors

Algorithm:
1. Create the feature vector
2. Create the distance function
3. Select an integer k > 0
4. For every point p to be predicted poll the k nearest neighbors and predict the non-location variables of p to the
   majority vote of the k nearest neighbors
   
"""

xo = [151, 174, 138, 186, 128, 136, 179, 163, 152, 131]
yo = [63, 81, 56, 91, 47, 57, 76, 72, 62, 48]

x = np.array(xo).reshape(-1, 1)
y = np.ravel(yo)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x, y)

pred = knn.predict(170)
print (pred)
