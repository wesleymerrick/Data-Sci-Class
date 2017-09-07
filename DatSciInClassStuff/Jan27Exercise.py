from __future__ import print_function
from collections import defaultdict as dd


"""
In class exercise from 1/27/17
"""

file = open('SoManyWords.txt', 'r')

word_count = dd(int)
stop = False

for line in file:  # inspired by/taken from http://stackoverflow.com/a/16922328
    for word in line.split():
        word_count[word] += 1

# inspired by/taken from http://stackoverflow.com/a/3177911
for word in sorted(word_count, key=word_count.get, reverse=True):
    print(word, word_count[word])
