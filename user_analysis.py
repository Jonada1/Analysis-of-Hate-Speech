from flask import Flask
from reddit_functions import get_subreddit_comments, get_hate_comments, \
    get_user_comments, find_total_intensity_of_comments, find_users_top_hate_word
from sentiment_analysis import sentiment_analyser, sentiment_polarity_printer

def get_user_comments_dictionary(hate_comments, hate_intensity):
    counter = 0
    user_comments_dictionary = dict()
    for hate_comment in hate_comments:
        counter = counter + 1
        if(counter == 10):
            break
        username = hate_comment.author
        user_comments = get_user_comments(username)
        user_hate_comments = get_hate_comments(user_comments, hate_intensity)
        user_comments_dictionary[username] = user_hate_comments
    return user_comments_dictionary


def analyse_user(subreddit_name, hate_intensity):
    subreddit_comments = get_subreddit_comments(subreddit_name)
    hate_comments = get_hate_comments(subreddit_comments, hate_intensity)
    f = open("subreddit_comments\\{0}_{1}_intensity.txt".format(subreddit_name, hate_intensity).encode('utf-8'), "w+")
    for comment in hate_comments:
        f.write("%s\r\n" % (comment.body).encode('utf-8'))
    f.close
    user_comments_dictionary = get_user_comments_dictionary(hate_comments, hate_intensity)
    for user, comments in user_comments_dictionary.items():
        user_intensity = find_total_intensity_of_comments(comments)
    
    if(len(comments) > 0):
        polarity_dictionaries = sentiment_analyser(comments)
        sentiment_polarity_printer(polarity_dictionaries)

        f = open("user_analysis\\{0}-{1}_intensity-{2}.txt".format(subreddit_name, hate_intensity, user), "w+")
        for comment in comments:
            f.write("%s\r\n" % (comment.body).encode('utf-8'))
            f.write("Intensity for user: %s\r\n" % (user_intensity))
            f.write("Top hate word: %s\r\n" % (find_users_top_hate_word(comments)[0]))
            f.write("Sentiment analysis: %s\r\n" % (sentiment_polarity_printer(polarity_dictionaries)))
        f.close

        
analyse_user("TalesFromYourServer", "high")
analyse_user("TalesFromYourServer", "medium")
analyse_user("TalesFromYourServer", "moderate")
