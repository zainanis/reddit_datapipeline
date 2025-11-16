from etls.reddit_etl import  extract_posts_public, load_data_to_csv, transform_data
from utils.constants import OUTPUT_PATH
import pandas as pd


def reddit_pipeline_v02(file_name:str,subreddit:str,limit=None):

    posts=extract_posts_public(subreddit,limit)

    post_df=pd.DataFrame(posts)

    post_df=transform_data(post_df)

    file_path=f"{OUTPUT_PATH}/{file_name}.csv" 
    load_data_to_csv(post_df,file_path)
    
    return file_path
