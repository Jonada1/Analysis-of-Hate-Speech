from reddit_functions import get_subreddit_comments, get_hate_comments, \
    get_user_comments, find_total_intensity_of_comments


def get_user_comments_dictionary(hate_comments, hate_intensity):
    counter = 0
    user_comments_dictionary = dict()
    for hate_comment in hate_comments:
        counter = counter + 1
        if(counter == 5):
            break
        username = hate_comment.author
        user_comments = get_user_comments(username)
        user_hate_comments = get_hate_comments(user_comments, hate_intensity)
        user_comments_dictionary[username] = user_hate_comments
    return user_comments_dictionary


def analyse_user(subreddit_name, hate_intensity):
    subreddit_comments = get_subreddit_comments(subreddit_name)
    hate_comments = get_hate_comments(subreddit_comments, hate_intensity)
    user_comments_dictionary = get_user_comments_dictionary(hate_comments, hate_intensity)
    for user, comments in user_comments_dictionary.items():
        user_intensity = find_total_intensity_of_comments(comments)
        print("Intensity for user :", user, user_intensity)




analyse_user("The_Donald", "high")
analyse_user("The_Donald", "medium")
analyse_user("The_Donald", "low")
# TODO: analyse user comments
