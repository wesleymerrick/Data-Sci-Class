from __future__ import print_function
from collections import defaultdict as dd
"""
Exercises and notes from 1/27/17
"""

# Tuples - immutable lists - parentheses rather than braces
x = (1, 2, 3, 4)
# can only concatenate tuples and with tuples

# Dictionaries - stored as key-value pairs
grades = {'Joel': 80, 'Tim': 95}
print(grades['Tim'])

# EXERCISE Generate frequency count of words in a text file
word_counts = dd(int)
document = ['Alan', 'Joe', 'Alan', 'Dave', 'Goober', 'Goober', 'Goober']
word_counts
