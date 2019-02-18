from flask import Flask
from reddit_functions import get_subreddit_comments, get_hate_comments, \
    get_user_comments, find_total_intensity_of_comments, find_users_top_hate_word
from sentiment_analysis import sentiment_analyser, sentiment_polarity_printer

app = Flask(__name__)
@app.route("/")
def hello():
    return "<table class='table table-striped table-hover'><tr><th> Task fg</th><tr></table>"


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


@app.route("/redditAnalyse")
def analyse_user(subreddit_name, hate_intensity):
    subreddit_comments = get_subreddit_comments(subreddit_name)
    hate_comments = get_hate_comments(subreddit_comments, hate_intensity)
    user_comments_dictionary = get_user_comments_dictionary(hate_comments, hate_intensity)
    for user, comments in user_comments_dictionary.items():
        user_intensity = find_total_intensity_of_comments(comments)
        print("***************************************************************************")
        print("User: ", user)
        print("Top hate word", find_users_top_hate_word(comments)[0])
        print("Intensity for user ", user_intensity)
        print("Comments", comments)

        f = open("user_analysis\\%s.txt" %str(user), "w+")
        for comment in comments:
            f.write("%s\r\n" % (comment.body))
        f.close

        if(len(comments) > 0):
            print("Sentiment analysis: ")
            polarity_dictionaries = sentiment_analyser(comments)
            sentiment_polarity_printer(polarity_dictionaries)
        print("**************************************************************************")


analyse_user("The_Donald", "high")
analyse_user("AskMen", "medium")
analyse_user("feminazi", "moderate")
