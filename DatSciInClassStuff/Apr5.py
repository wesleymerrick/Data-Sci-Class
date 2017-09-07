"""
Support Vector Machines

A binary linear classifier designed to create a gap of maximum possible width between two clusters
Data set can be adjusted (kernel function) to make the maximal separation appear linear

Algorithm:
1) Choose a binary variable to predict
2) Select the predicting variables from the data set and create a training set
3) From the training set, calculate separating lines/planes/hyperplanes
4) Select the optimal divider based on a distance function from the support vector
"""

from __future__ import print_function
from sklearn import svm

x = [[0, 0], [1, 1]]  # data set
y = [0, 1]  # possible binary calas values
c = svm.SVC()
c.fit(x, y)
print(c.predict([[2, 2]]))
