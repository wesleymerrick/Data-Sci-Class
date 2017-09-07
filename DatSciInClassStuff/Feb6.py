from __future__ import print_function
# pip install numpy
import numpy as np
"""
Exercises and notes from 2/6/17
"""

# Calculate the following quantile values for LotsofNums.txt: 10%, 25%, 50%, 75%, 90%, 95%, and 99%

# print("The 10th quantile is: ", np.percentile(np.asanyarray(numbers, dtype=int), 10, interpolation='midpoint'))
# print("The 25th quantile is: ", np.percentile(np.asanyarray(numbers, dtype=int), 25, interpolation='midpoint'))
# print("The 50th quantile is: ", np.percentile(np.asanyarray(numbers, dtype=int), 50, interpolation='midpoint'))
# print("The 75th quantile is: ", np.percentile(np.asanyarray(numbers, dtype=int), 75, interpolation='midpoint'))
# print("The 90th quantile is: ", np.percentile(np.asanyarray(numbers, dtype=int), 90, interpolation='midpoint'))
# print("The 95th quantile is: ", np.percentile(np.asanyarray(numbers, dtype=int), 95, interpolation='midpoint'))
# print("The 99th quantile is: ", np.percentile(np.asanyarray(numbers, dtype=int), 99, interpolation='midpoint'))


def de_mean(mean, data):
    return data - mean


def sum_of_squares(mean, devs):
    ss = 0
    for d in devs:
        ss += (d - mean)**2
    return ss


def variance(x):
    n = len(x)
    tot = 0
    for j in x:
        tot += int(j)
    mean = tot / n
    deviations = []
    for d in x:
        deviations.append(de_mean(mean, d))

    return sum_of_squares(mean, deviations)/(n-1)

# Main method
if __name__ == '__main__':
    num_list = open('LotsofNums.txt', 'r')

    numbers = []

    for i in range(20):
        line = num_list.readline()
        for num in line.split():
            numbers.append(int(num))

    print("The variance is :", variance(numbers))
    print("The standard deviation is: ", (variance(numbers))**.5)
