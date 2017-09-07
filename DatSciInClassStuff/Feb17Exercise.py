from __future__ import print_function
import urllib
from matplotlib import pyplot as plt
"""
Exercises from 2/17/17
"""

text = urllib.urlopen("http://ripark.github.io/s17/Acorns.txt")
nums = urllib.urlopen("http://ripark.github.io/s17/LotsofNums.txt")

species = []
reg_lbls = []
rnge = []
acorn_size = []
tree_height = []
atlantic = []
california = []
numbers = []

line_ctr = 0

for line in text:
    words_in_line = line.split('\t')
    if line_ctr != 0:
        if words_in_line[1] == "Atlantic":
            atlantic.append(1.0)
            reg_lbls.append('A')
        else:
            atlantic.append(0.0)
            reg_lbls.append('C')
        if words_in_line[1] == "California":
            california.append(1.0)
        else:
            california.append(0.0)
        species.append(words_in_line[0])
        rnge.append(words_in_line[2])
        acorn_size.append(words_in_line[3])
        tree_height.append(words_in_line[4])

    line_ctr += 1

for line in nums:
    for num in line.split():
        numbers.append(num)

plt.boxplot(numbers)
plt.show()
for i in nums:
    plt.plot(1, i, 'ro')

# print("Size of acorn size list: ", len(acorn_size))
# print("Size of tree height list: ", len(tree_height))
# print("Size of range list: ", len(rnge))
# print("Size of labels list: ", len(reg_lbls))
#
# my_zip = zip(reg_lbls, tree_height, acorn_size)
#
# plt.scatter(tree_height, acorn_size)  # Plot tree height vs. acorn size
# for reg_lbls, tree_height, acorn_size in my_zip:
#     plt.annotate(reg_lbls, xy=(tree_height, acorn_size))
# plt.show()
#
# plt.scatter(tree_height, rnge)  # Plot tree height vs. range
# for reg_lbls, tree_height, rnge in my_zip:
#     plt.annotate(reg_lbls, xy=(tree_height, rnge))
# plt.show()
#
# plt.scatter(acorn_size, rnge)  # Plot acorn size vs. range
# for reg_lbls, acorn_size, rnge in my_zip:
#     plt.annotate(reg_lbls, xy=(acorn_size, rnge))
# plt.show()
