from __future__ import print_function
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import tweepy

"""
TwitterDataVis.py
Contains functions to pull tweets from twitter with a specified hashtag or other string provided the user has an
appropriate Keys.txt file in the same directory as this file. Other functions included take those pulled tweets and
print statistics such as most favorited tweet and the user with the most tweets pulled with the hashtag specified.
Another function can take a frequency list of tweets containing a certain hashtag in six hour intervals and create a
bar graph from that information.
Toby Duncan and Wesley Merrick
Miniproject 2
COSC 480 - 01
03/03/2017
"""

f = open("Keys.txt")
# Setting up all the authentication for twitter app via Keys.txt doc
consumer_key = f.readline().strip()
consumer_secret = f.readline().strip()
app_key = f.readline().strip()
app_secret = f.readline().strip()
# Setting up tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(app_key, app_secret)
# Ensure tweepy will to continue rather than exit if the rate limit is reached
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def ingest_tweets(tag):
    """
    Returns a list of all tweets returned from calling tweepy's api.search on the passed in string tag between
    Febuary 24th and Febuary 29th, exclusive.
    """
    more_tweets = True  # Weather to continue searching, True while all 100 results on page are in time range specified
    iteration = 0  # Count the pages returned
    parsed_results = []  # Collect all tweets into a single list to return

    while more_tweets:
        if iteration is 0:  # Don't need to specify max_id= on first run
            results = api.search(q=tag + " since:2017-02-24", count=100, until='2017-02-028')
            iteration += 1
        else:  # Specify max_id= on all subsequent runs
            results = api.search(q=tag + " since:2017-02-24", count=100, until='2017-02-28', max_id=max_id)
            iteration += 1

        if len(results) != 0:
            for i in range(0, len(results)):  # Parse and append all tweets to the parsed_tweets list
                parsed_results.append(results[i]._json)
            if parsed_results[(len(parsed_results) - 1)][u'created_at'][7:9] > 25:
                max_id = parsed_results[len(parsed_results) - 1][u'id'] - 1  # If so, update max_id to use in next query

        else:
            more_tweets = False  # Stop looping when results in desired time frame are exhausted

    print("Finished ingestion after", iteration, "iterations")
    print("Collected", len(parsed_results), "tweets containing", tag)
    print("First tweet pulled was posted on: ", parsed_results[0][u'created_at'])
    print("Last tweet pulled was posted on: ", parsed_results[len(parsed_results) - 1][u'created_at'])
    return parsed_results


def hashtag_stats(parsed_results, tag):
    """
    method that prints out the hashtag stats most frequent user, user with most followers, tweet with most retweets,
    and tweet with the most favorites
    :param parsed_results: list of all parsed tweets returned from a call to ingest_tweets()
    :param tag: the hashtag searched for in the ingest_tweets() call, passed in for printing only
    """
    users = []  # list to hold all the users

    # loops through parsed results and stores all the user data in the list users
    for i in range(0, len(parsed_results)):
        users.append(str(parsed_results[i][u'user'][u'screen_name']))

    most_common_tuple = Counter(users).most_common(1)  # Inspired by http://stackoverflow.com/a/5829377
    most_common_dict = dict((y, x) for x, y in most_common_tuple)

    # printing most common user
    print()
    print("The most commonly appearing user tweeting", tag, "was", most_common_dict.values()[0], "with",
          most_common_dict.keys()[0], "total tweets.")
    print()

    # finding and printing user with the most followers
    user_followers = {}  # dictionary which holds the users and the number of followers they have

    # loops through the parsed results from api.search getting the user data
    for i in range(0, len(parsed_results)):
        user_followers[parsed_results[i][u'user'][u'followers_count']] = parsed_results[i][u'user'][u'screen_name']

    # follower counts getting set to the amount of followers per user
    follower_counts = user_followers.keys()

    most_followers = 0

    # finding the user with the largest follower count
    for j in range(0, len(follower_counts)):
        if follower_counts[j] > most_followers:
            most_followers = follower_counts[j]

    # printing out the user with the most followers
    print("User", user_followers[most_followers], "tweeting", tag, "had the most followers with", most_followers,
          "followers.")
    print()

    tweet_favorites = {}  # dictionary to hold each users and how many retweets they have

    # loops through tweet_favorites getting the text for each result
    for i in range(0, len(parsed_results)):
        tweet_favorites[parsed_results[i][u'favorite_count']] = parsed_results[i][u'text']

    # setting favorite counts to all the favorite counts of the different tweets
    favorite_counts = tweet_favorites.keys()

    most_favorites = 0

    # loops through each of the favorite counts to find the biggest favorite count
    for j in range(0, len(favorite_counts)):

        if favorite_counts[j] > most_favorites:
            most_favorites = favorite_counts[j]

    # printing out the tweet with the most favorites
    print("The following tweet containing", tag, ":\n", tweet_favorites[most_favorites], "\n",
          "had the most favorites with", most_favorites, "favorites.")
    print()

    # dictionary to hold each tweet and the number of retweets it had
    retweets = {}

    # loops through the parsed_results getting each tweet
    for i in range(0, len(parsed_results)):
        retweets[parsed_results[i][u'retweet_count']] = parsed_results[i][u'text']

    retweet_counts = retweets.keys()  # stores the count of num of retweets in the list retweet_counts

    most_retweets = 0

    # loops through retweet_counts, finding the tweet with the most retweets
    for j in range(0, len(retweet_counts)):
        if retweet_counts[j] > most_retweets:
            most_retweets = retweet_counts[j]

    # printing out the tweet with the most retweets
    print("The following tweet containing", tag, ":\n", retweets[most_retweets], "\n",
          "had the most retweets with", most_retweets, "retweets.")
    print()


def get_chart_data(parsed_results):
    """
    Formats the data in parsed_results into a frequency list over six-hour intervals
    :param parsed_results: list of all parsed tweets returned from a call to ingest_tweets()
    :return: a frequency list for tweets in each of the 16 six-hour intervals across the four day span Feb 25-28th
    """
    dates = []  # list that holds all the raw tweets dates they were created
    dates_fixed = []  # list that holds all the cleaned up tweet dates they were created

    # getting the raw date created data for each tweet
    for i in range(0, len(parsed_results)):
        dates.append(str(parsed_results[i][u'created_at']))

    # appendind the dates in order to get just the time and day it was created
    for i in range(0, len(dates)):
        temp = dates[i]
        dates_fixed.append(temp[4:19])

    # printing out all the fixed dates created for each tweet

    for j in range(0, len(dates_fixed)):  # Adjusting GMT to EST(GMT-5)
        if int(dates_fixed[j][7:9]) < 5:  # Check if convecting time zone will change the day
            # Change the timestamp accordingly
            hr = 5 - int(dates_fixed[j][7:9])
            hr = 24 - hr
            dates_fixed[j] = "Feb " + str(int(dates_fixed[j][4:6]) - 1) + " " + str(hr) + str(dates_fixed[j][9:19])
        else:  # Decrement the hours in the timestamp by 5 to convert to EST
            dates_fixed[j] = "Feb " + str(int(dates_fixed[j][4:6])) + " " + str(dates_fixed[j][7:9]) +\
                             str(dates_fixed[j][9:16])

    # lists to store each tweet created on a specific day
    feb25 = []
    feb26 = []
    feb27 = []
    feb28 = []

    # loops through the dates_fixed list putting each tweet into the list of the appropriate day it was created
    for i in range(0, len(dates_fixed)):
        temp = dates_fixed[i]
        temp = temp[4:6]
        full_time = dates_fixed[i][7:12]
        if int(temp) == 28:
            feb28.append(full_time)
        elif int(temp) == 27:
            feb27.append(full_time)
        elif int(temp) == 26:
            feb26.append(full_time)
        elif int(temp) == 25:
            feb25.append(full_time)

    output = []  # list to store the data broken into blocks

    days = [feb25, feb26, feb27, feb28]

    # looping through the date data and storing it in blocks of 6 hours
    for i in range(0, len(days)):
        if len(days[i]) is not 0:
            # Temporary variables to store the number of tweets created in each 1/4th (6 hr interval) of each day
            q1 = 0
            q2 = 0
            q3 = 0
            q4 = 0
            for j in range(0, len(days[i])):  # Iterate over each day's list (i.e. feb25 then feb26, etc.)
                element = int(days[i][j][0:2])
                if element >= 0 and element < 6:  # Increment the frequency in the appropriate 6hr interval
                    q1 += 1
                elif element >= 6 and element < 12:
                    q2 += 1
                elif element >= 12 and element < 18:
                    q3 += 1
                elif element >= 18 and element < 24:
                    q4 += 1
            # Add frequency lists for each six-hour interval to the output list for the day being iterated over
            output.append(q1)
            output.append(q2)
            output.append(q3)
            output.append(q4)

    return output



def make_graph(freq_list, tag):
    """
    Creates a bar graph displaying the 16 valuse in freq_list
    :param freq_list: the frequency list produced by a previous call to get_chart_data()
    :param tag: the hashtag searched for in the ingest_tweets() call, passed in for labeling
    """
    # Inspiration for bar graphs in pyplot taken from: http://matplotlib.org/examples/api/barchart_demo.html
    # setting up bar graph
    n = len(freq_list)
    ind = np.arange(n)
    fig, g = plt.subplots()
    width = .35

    g.bar(ind, freq_list, width, color='r')  # Define the bars' parameters
    g.set_xlabel('Time')
    g.set_ylabel('Frequency')
    g.set_xticks(ind)
    g.set_title(tag)
    g.set_xticklabels(("(Feb25)0:00-5:59", "6:00-11:59", "12:00-17:59", "18:00-23:59",
                       "(Feb26)0:00-5:59", "6:00-11:59", "12:00-17:59", "18:00-23:59",
                       "(Feb27)0:00-5:59", "6:00-11:59", "12:00-17:59", "18:00-23:59",
                       "(Feb28)0:00-5:59", "6:00-11:59", "12:00-17:59", "18:00-23:59",))

    plt.tight_layout()
    plt.show()  # display the graph


if __name__ == '__main__':
    tags = ["#csforall", "#equality", "#equity", "#stem", "#yolo"]
    for i in range(0, len(tags)):
        # Call ingest_tweets only once for each hashtag to avoid the rate limit as much as possible
        current_tag = ingest_tweets(tags[i])
        hashtag_stats(current_tag, tags[i])
        make_graph(get_chart_data(current_tag), tags[i])
