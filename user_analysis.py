from reddit_functions import get_subreddit_comments, get_hate_comments, \
    get_user_comments


def analyse_user(subreddit_name, hate_intensity):
    subreddit_comments = get_subreddit_comments(subreddit_name)
    hate_comments = get_hate_comments(subreddit_comments, hate_intensity)
    for hate_comment in hate_comments:
        username = hate_comment.author
        try:
            user_comments = get_user_comments(username)
            for comment in user_comments:
                print(comment.body)
        except Exception:
            # Do nothing
            print("Boiiiii")


analyse_user("UltraViolent", "high")
analyse_user("UltraViolent", "medium")
analyse_user("UltraViolent", "low")
# TODO: analyse user comments
