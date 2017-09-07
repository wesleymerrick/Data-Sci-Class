from __future__ import print_function
import re  # regular expression of x
"""
Exercises and notes from 1/30/17
"""

my_list = {1, 3, 4}
sorted(my_list)  # creates a new sorted list without modifying the ordinal list
# list.sort()  # sorts in place

# Lambda expressions - one time applications to data
g = lambda x: x+2
print('g =', g(9))

a = range(100)
print(filter(lambda x:x % 2 == 0, a))

print(re.sub("[0-9]", "!", "n00bl33t"))
