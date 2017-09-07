from __future__ import print_function
import urllib
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
text = urllib.urlopen("http://ripark.github.io/s17/Acorns.txt")

rnge = []
acorn_size = []
tree_height = []

line_ctr = 0

for line in text:
    words_in_line = line.split('\t')
    if line_ctr != 0:
        rnge.append(float(words_in_line[2]))
        acorn_size.append(float(words_in_line[3]))
        tree_height.append(float(words_in_line[4]))

    line_ctr += 1

# print (rnge)
# print ("Tree height:")
# print (tree_height[4])
# print (len(tree_height))
# print ("Acorn size:")
# print (acorn_size[4])
# print (len(acorn_size))

x = [int(i * 10) for i in tree_height]
y = [int(i * 10) for i in acorn_size]


xa = np.array(x).reshape(-1, 1)
ya = np.ravel(y)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(xa, ya)

pred = knn.predict(240)
print ("Predicted acorn size for a tree 24 (units) tall: ", int(pred))
