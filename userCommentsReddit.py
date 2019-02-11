import praw

user_name = "Lavishlust"
user_agent = "subreddit analyzer"

r = praw.Reddit(user_agent=user_agent,
                        client_id='hH4pioFdIqPqTg', client_secret="U4Xu1kraO2HdF8Xr5xLhNPHA8cA")
user = r.redditor('ketralnis')
print('praw version: {}'.format(praw.__version__))

for comment in user.comments.new():
    print(comment.body)

submission = r.submission(id='16m0uu')
comment = submission.comments[0] ##index needed
author = comment.author  # This returns a ``Redditor`` object.
print(author.name)  # The username 