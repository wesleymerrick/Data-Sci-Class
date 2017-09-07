from __future__ import print_function
from bs4 import BeautifulSoup
import urllib
import re

# WebScraper.py
# Toby Duncan and Wesley Merrick
# COSC 480 - 01
# Mini Project 1
# 2/10/17

# List that holds the url's for each of the articles to scrape
my_url_list = ["http://www.theonion.com/article/sixth-super-bowl-win-continues-elude-patriots-55231",
               "http://www.theonion.com/article/lady-gaga-panics-after-hearing-name-called-halftim-55234",
               "http://www.theonion.com/article/father-teaches-son-how-shave-him-55223",
               "http://www.theonion.com/article/burmese-python-shocked-amount-stress-man-holding-h-55196",
               "http://www.theonion.com/article/trump-supporter-has-few-backup-scapegoats-ready-go-55186",
               "http://www.theonion.com/article/mom-just-wants-watch-something-nice-55183",
               "http://www.theonion.com/article/nothing-would-surprise-me-point-says-man-who-will--55179",
               "http://www.theonion.com/article/it-too-late-audition-asks-perfect-actor-role-pokin-55176",
               "http://www.theonion.com/article/2-year-old-unaware-hes-basis-6-couples-decisions-n-55166",
               "http://www.theonion.com/article/man-spends-whole-day-dreading-fun-activity-he-sign-55165",  # 10
               "http://www.theonion.com/article/explanation-board-game-rules-peppered-reassurances-55162",
               "http://www.theonion.com/article/man-chippewa-falls-wisconsin-hates-when-people-eag-55157",
               "http://www.theonion.com/article/spider-sitting-shower-wall-cant-wait-see-look-mans-55136",
               "http://www.theonion.com/article/asshole-moves-part-city-where-all-assholes-live-55074",
               "http://www.theonion.com/article/32-year-old-still-not-entirely-sure-where-body-sta-55057",
               "http://www.theonion.com/article/7-year-old-apparently-under-impression-everyone-kn-55027",
               "http://www.theonion.com/article/man-excited-spend-weekend-back-home-catching-old-v-55019",
               "http://www.theonion.com/article/mom-nightgown-mode-55001",
               "http://www.theonion.com/article/controversial-puppy-bowl-star-shits-during-nationa-55240",
               "http://www.theonion.com/article/area-man-totally-screwing-order-snack-consumption--55237",
               ]


# Scrape all url's for the article's body text, then calculate and return the number a list # of words per article
# and a list of all words found across all articles, counting repeats
def scrape_word_counts(url_list):
    all_words = []  # List of all words found across all articles
    words_per_article = []  # List to hold the word count of each separate article
    for l in url_list:
        tmp_wpa = 0  # Counter for number of words in each article, set counter to zero at the start of each article
        r = urllib.urlopen(l)  # sets the contents of the open url to r
        soup = BeautifulSoup(r, "html.parser")  # bs4 object, default html parser specified

        stuff = soup.find('p').get_text()  # Getting text inside paragraph tags for each article
        for word in stuff.split():  # Separate scraped text into individual words
            word = re.sub(r'[^\w]', '', word)  # Strip all punctuation FIXME: don't strip apostrophes
            all_words.append(word)  # Add formatted word to the list of all scraped words
            tmp_wpa += 1  # Increment the number of words found in the current article

        # Add the number of words found to the appropriate list after scraping each article
        words_per_article.append(tmp_wpa)

    return words_per_article, all_words


# Calculate and return the mean and median # of words per article
def mid_count(words_in_article):
    running_sum = 0  # Counts up the number of words
    for ct in words_in_article:
        running_sum += ct  # Sum the word counts of all articles
    mean = running_sum / len(my_url_list)  # Calculate the mean word count per article
    words_in_article.sort()  # Sort the list to make finding the median easy
    # Calculate the median word count per article
    if len(words_in_article) % 2 == 0:
        median = (words_in_article[(len(words_in_article) / 2)]
                  + words_in_article[(len(words_in_article) / 2) + 1] / 2)
    else:
        median = words_in_article[(len(words_in_article) / 2)]

    return mean, median


# Calculate and print the most frequently used word (or words if it's a tie)
def freq_list(word_list):
    # imports defaultdict to use to make frequency list
    from collections import defaultdict as dd

    word_counts = dd(int)  # instance of defaultdict

    # loops through word_list making frequency list
    for word in word_list:
        word_counts[word] += 1

    individual_words = []  # list to hold sorted words
    individual_count = []  # list to hold number of times each word was found

    # http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
    # sorts list and appends the two lists to hold the most frequent word and number of times it shows up
    # in descending order
    for w in sorted(word_counts, key=word_counts.get, reverse=True):
        individual_words.append(w)
        individual_count.append(word_counts[w])

    # Prints the most frequent word (or words if it's a tie) and how many times it shows up
    if individual_count[0] == individual_count[1]:  # Case where two or more words are tied for most frequent
        freq_words = individual_words[0]  # String to hold all words tied for most frequent
        k = 1
        while individual_count[k] == individual_count[0]:  # Find most frequent words (works because of earlier sort)
            freq_words = freq_words + ", " + individual_words[k]
            k += 1
        print("The most frequently used words were: \"" + freq_words + "\" with " + str(individual_count[0])
              + " usages each")
    else:  # Case where there is only one most frequently used word
        print("The most frequently used word was: \"" + (individual_words[0]) + "\" with "
              + str(individual_count[0]) + " usages")

# prints the remaining words
    print("The following is a frequency list of all other words in descending order:\n")
    # http://stackoverflow.com/questions/1663807/how-can-i-iterate-through-two-lists-in-parallel-in-python
    for a, b in zip(individual_words[0:], individual_count[0:]):
        if b == 1:  # Handle pluralization
            print(a + " - " + str(b) + " usage")
        else:
            print(a + " - " + str(b) + " usages")

# Main method
if __name__ == '__main__':
    words_per, words_master = scrape_word_counts(my_url_list)  # Assign local variables so we can call other methods
    avg, med = mid_count(words_per)  # Calculate the mean and median number of words per article scraped
    # Print those results
    print("The average (mean) number of words in each article was: ", avg)
    print("The median number of words in each article was: ", med)
    freq_list(words_master)  # Generate and print frequency list of words found across all articles
