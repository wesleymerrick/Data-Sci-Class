from __future__ import print_function
import urllib
import math
"""
Exercise from 2/13/17
"""

text = urllib.urlopen("http://ripark.github.io/s17/Acorns.txt")

rnge = []
acorn_size = []
tree_height = []
atlantic = []
california = []

line_ctr = 0

for line in text:
    words_in_line = line.split('\t')
    if line_ctr != 0:
        if words_in_line[1] == "Atlantic":
            atlantic.append(1.0)
        else:
            atlantic.append(0.0)
        if words_in_line[1] == "California":
            california.append(1.0)
        else:
            california.append(0.0)
        rnge.append(words_in_line[2])
        acorn_size.append(words_in_line[3])
        tree_height.append(words_in_line[4])

    line_ctr += 1


def to_floats(inpt):
    output = []
    for i in inpt:
        output.append(float(i))
    return output


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


def covariance(x, y):
    n = len(x)
    return (variance(x) * variance(y)) / (n - 1)


def correlation(x, y):
    n = len(x)
    sum_x = 0
    sum_y = 0
    sum_x_sq = 0
    sum_y_sq = 0
    sum_xy = 0
    index = 0

    for i in x:
        sum_x += x[index]
        sum_x_sq += (x[index])**2
        sum_xy += x[index]*y[index]
        sum_y += y[index]
        sum_y_sq += (y[index])**2
        index += 1

    print(sum_x_sq)
    print(math.pow(sum_x, 2))
    r = n * (sum_xy - sum_x * sum_y) / math.sqrt(math.fabs(n * (sum_x_sq - math.pow(sum_x, 2))))\
        * math.sqrt(math.fabs(n * (sum_y_sq - math.pow(sum_y, 2))))
    # https://www.mathsisfun.com/data/correlation.html

    return r

if __name__ == '__main__':
    rnge = to_floats(rnge)
    acorn_size = to_floats(acorn_size)
    tree_height = to_floats(tree_height)
    print("The correlation between acorn size and tree height: ", correlation(acorn_size, tree_height))
