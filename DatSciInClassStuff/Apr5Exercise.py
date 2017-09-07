from __future__ import print_function
import csv
import numpy as np
from sklearn import svm

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

x = []
y = []

for k in range(0, 400):  # train on the first 400 data points
    x.append([all_data[k][0], all_data[k][2]])
    y.append(all_data[k][1])

np_x = np.asarray(x)
np_y = np.asarray(y)

c = svm.SVC()
c.fit(np_x, np_y)
print(c.predict([[20, 8]]))  # predict gender (0 or 1) for a 20 year-old individual with 8 impressions
