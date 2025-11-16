import sys
import requests
import pandas as pd
import numpy as np





def extract_posts_public(subreddit:str,limit:None):
    reddit_subreddit_path =f"https://www.reddit.com/r/{subreddit}/new.json?limit={limit}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    params = {}
    if limit:
        params['limit'] = limit
    
    try:
        response = requests.get(reddit_subreddit_path, headers=headers, params=params)
        response.raise_for_status()  
        
        # Fix: Use .json() instead of .data
        data = response.json()
        post_lists=[]
        print("Extracting post")
        for post in data["data"]["children"]:
            post_data = post["data"]
            post_info = {
            "id": post_data["id"],
            "title": post_data["title"],
            # "self_text":post_data["selftext"],
            "score": post_data["score"],
            "num_comments": post_data["num_comments"],
            "author":post_data["author"],
            "created_utc":post_data["created_utc"],
            "url": post_data["url"],
            # "upvote_ratio": post_data["upvote_ratio"],
            "over_18": post_data["over_18"],
            "edited": post_data["edited"],
            "spoiler": post_data["spoiler"],
            "stickied": post_data["stickied"],
            }
            post_lists.append(post_info)

        return post_lists
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Reddit: {e}")
        return None

def transform_data(post_df:pd.DataFrame):
    post_df['created_utc'] = pd.to_datetime(post_df['created_utc'], unit='s')
    post_df['over_18'] = np.where((post_df['over_18'] == True), True, False)
    post_df['author'] = post_df['author'].astype(str)
    edited_mode = post_df['edited'].mode()
    post_df['edited'] = np.where(post_df['edited'].isin([True, False]),
                                 post_df['edited'], edited_mode).astype(bool)
    post_df['num_comments'] = post_df['num_comments'].astype(int)
    post_df['score'] = post_df['score'].astype(int)
    post_df['title'] = post_df['title'].astype(str)
    return post_df

def load_data_to_csv(data:pd.DataFrame,path:str):
    data.to_csv(path,index=False)
