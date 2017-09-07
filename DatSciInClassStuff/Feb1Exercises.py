from __future__ import print_function
import re  # regular expression of x
"""
Exercises from 2/1/17
"""


# Exercise 1: create a function that reads in a string from the user and prints True or False depending on whether the
#              following patterns are matched
#
# Case 1: ab
# Case 2: abb or abbb
# Case 3: a followed by any number of characters, string ends in a b
# Case 4: any case insensitive vacations of the above 3 cases
# Case 5: string ends in one of the following characters: .1?
# Case 6: string contains only upper case letters, lower case letters, and numbers


def evalu8():
    results = {'ab': False, 'abb or abbb': False, 'a ending with ab': False, 'case insensitive': False,
               '.!? terminating': False, 'alphanumeric only': False}

    inpt = raw_input("Enter the string to be tested")

    if re.search("^ab$", inpt) is not None:
        results['ab'] = True

    if re.search("^abb$", inpt) or re.search("^abbb$", inpt) is not None:
        results['abb or abbb'] = True

    if re.search("^a.*ab$", inpt) is not None:  # FIXME: only works for ending in 'ab', not for 'a b'
        results['a ending with ab'] = True

    if re.search("^ab$", inpt, re.I) or re.search("^abb$", inpt, re.I) or re.search("^abbb$", inpt, re.I)\
            or re.search("^a.*ab$", inpt, re.I) is not None:
        results['case insensitive'] = True

    if re.search("[.!?]$", inpt) is not None:
        results['.!? terminating'] = True

    if re.search("[\W_]", inpt) is None:
        results['alphanumeric only'] = True

    print('Test 1: ', results['ab'], '\n')
    print('Test 2: ', results['abb or abbb'], '\n')
    print('Test 3: ', results['a ending with ab'], '\n')
    print('Test 4: ', results['case insensitive'], '\n')
    print('Test 5: ', results['.!? terminating'], '\n')
    print('Test 6: ', results['alphanumeric only'], '\n')


# Exercise 2: Create a function that returns all five letter words in a string input by the user


def five_letter():
    five_ltr_words = []
    inpt = raw_input("Input a string of words: ")
    for word in inpt.split():
        if word.__len__() == 5:
            five_ltr_words.append(word)

    return five_ltr_words

# Exercise 3: Create a function that returns a string of all characters found between quotation marks with each set of
#             characters separated by a newline


def xtract_quotes():
    inpt = raw_input("Input a string: ")
    results = re.findall(r'"(.+?)"', inpt)
    for result in results:
        print(result)

# Main method
if __name__ == '__main__':
    evalu8()
    # print(five_letter())
    # xtract_quotes()
