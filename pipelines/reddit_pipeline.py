from etls.reddit_etl import connect_reddit, extract_posts, extract_posts_public
from utils.constants import CLIENT_ID, REDDIT_SUBREDDIT_PATH, SECRET

def reddit_pipeline(file_name:str,subreddit:str,time_filter='day',limit=None):
    instance=connect_reddit(CLIENT_ID,SECRET,'Airscholar Agent')
    posts=extract_posts(instance,subreddit,time_filter,limit)
    return

def reddit_pipeline_v02(limit=None):
    posts=extract_posts_public(REDDIT_SUBREDDIT_PATH,limit)
    return
