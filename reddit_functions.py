import praw
import nltk
from ProgramIntensity import high_intensity_words
from ProgramIntensity import medium_intensity_words, moderate_intensity_words

reddit = praw.Reddit(
    user_agent='Comment Extraction (by /u/USERNAME)',
    client_id='hH4pioFdIqPqTg', client_secret="U4Xu1kraO2HdF8Xr5xLhNPHA8cA"
)


def get_subreddit_comments(subredditName):
    subreddit = reddit.subreddit(subredditName)
    comment_array = []
    for submission in subreddit.hot(limit=10):
        comments = submission.comments
        for comment in comments:
            comment_array.append(comment)
    return comment_array


def does_comment_have_hate_words(comment, hate_words):
    if(hasattr(comment, "body")):
        words = nltk.word_tokenize(comment.body)
        for word in words:
            if (word in hate_words):
                return True
    else:
        return False


def get_hate_comments(comment_array, intensity):
    hate_comments = []
    hate_words = get_hate_words_by_intensity(intensity)
    for comment in comment_array:
        if(does_comment_have_hate_words(comment, hate_words)):
            hate_comments.append(comment)
    return hate_comments


def get_hate_words_by_intensity(intensity):
    if(intensity == "high"):
        return high_intensity_words
    elif(intensity == "medium"):
        return medium_intensity_words
    else:
        return moderate_intensity_words


def get_user_comments(username):
    print(username)
    user = reddit.redditor("ketralnis")
    return 
    print(user)
    print("Fails 1")
    comments = user.comments.new()
    print("Fails 2")
    return comments
