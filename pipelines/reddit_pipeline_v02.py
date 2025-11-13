from etls.reddit_etl import  extract_posts_public
from utils.constants import REDDIT_SUBREDDIT_PATH



def reddit_pipeline_v02(limit=None):
    print("hello")
    posts=extract_posts_public(REDDIT_SUBREDDIT_PATH,limit)
    return
