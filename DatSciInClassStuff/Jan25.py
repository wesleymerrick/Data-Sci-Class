from __future__ import print_function
import random
import math
"""
Exercises and notes from 1/25/17
"""


# Exercise 1
def addorsub(x, a, b):

    if x == 0:
        return a + b
    elif x == 1:
        return a - b
    else:
        return 'Please use a 0 or 1 when selecting an operation'

# Other notes
myList = {'cat', 'window', 'someLongWord'}

for item in myList:
    print(item)
    print(len(item))

for i in range(10):
    print(i)


# Exercise 2
def facts(x):
    return math.factorial(x)

print('Factorial of 3 is', facts(3))

# Lists
list2 = [4, 5, 6, 7]
mySlice = list2[1:3]  # Slice from first element, inclusive, to 3rd element, exclusive


# Excercise 3
def rand_range(x, y):
    list_out = []
    for num in range(0, x):
        list_out.append(random.randrange(0, y))

    return list_out

# Main method
if __name__ == '__main__':
    # print(addorsub(input('Enter 0 for addition, 1 for subtraction: '), input('Enter first integer: '),
    #                input('Enter second integer: ')))

    # print(facts(input('Enter integer to find factorial of: ')))

    print(rand_range(4, 5))
