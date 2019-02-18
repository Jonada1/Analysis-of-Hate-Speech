import praw
import nltk
from ProgramIntensity import high_intensity_words, get_all_words_with_intensity
from ProgramIntensity import medium_intensity_words, moderate_intensity_words
import collections

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
    return False


def get_hate_comments(comment_array, intensity):
    hate_comments = []
    hate_words = list(map(lambda x: x.word, get_all_words_with_intensity()))
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
    user = reddit.redditor(str(username))
    comments = user.comments.new(limit=10)
    return comments


def find_hate_words(text):
    hWords = list(map(lambda x: x.word, get_all_words_with_intensity()))
    results = []
    words = nltk.word_tokenize(text)
    for word in words:
        if (word in hWords):
            results.append(word)
    return results

def find_total_intensity_of_words(words):
    total_intensity = 0
    for word in words:
        intensity = list(filter(lambda x: x.word == word, get_all_words_with_intensity()))[0].intensity
        total_intensity += intensity
    return total_intensity

def find_total_intensity_of_comments(hate_comments):
    total_intensity = 0
    for comment in hate_comments:
        comment_hate_words = find_hate_words(comment.body)
        total_intensity += find_total_intensity_of_words(comment_hate_words)
    return total_intensity


def find_users_top_hate_word(comments):
    all_hate_words = []
    for comment in comments:
        hate_words = find_hate_words(comment.body)
        for word in hate_words:
            all_hate_words.append(word)
    most_common = collections.Counter(all_hate_words).most_common(1)
    return most_common