from __future__ import print_function
import csv
from matplotlib import pyplot

"""
Exercise from 2/2717
"""

file_names = []

for i in range(1, 32):
    file_names.append('nyt' + str(i) + '.csv')

file_names.append('rollingsales_bronx.csv')
file_names.append('rollingsales_brooklyn.csv')
file_names.append('rollingsales_manhattan.csv')
file_names.append('rollingsales_queens.csv')
file_names.append('rollingsales_statenisland.csv')

all_data = []

for i in file_names:
    with open('Feb27Data\\' + str(i)) as csvfile:
        reader = csv.DictReader(csvfile)
        print('Added ' + str(i))
        all_data += list(reader)

print(all_data)
