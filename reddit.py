import praw

def reddit_post_analyzer(post_url, reddit_client_id, reddit_client_secret, reddit_user_agent):
    reddit = praw.Reddit(client_id=reddit_client_id,
                         client_secret=reddit_client_secret,
                         user_agent=reddit_user_agent)
    
    submission = reddit.submission(url=post_url)
    
    comments_sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}

    for comment in submission.comments:
        if comment.score > 0:
            comments_sentiments['positive'] += 1
        elif comment.score < 0:
            comments_sentiments['negative'] += 1
        else:
            comments_sentiments['neutral'] += 1

    return comments_sentiments