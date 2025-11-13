import praw
from praw import Reddit
import sys
import requests

def connect_reddit(client_id,client_secret,user_agent)->Reddit:
    try:
        reddit=Reddit(client_id,client_secret,user_agent)
        print("connected to reddit")
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)

def extract_posts(reddit_instance:Reddit,subreddit:str,time_filter:str,limit:None):
    subreddit=reddit_instance.subreddit(subreddit)
    posts=subreddit.top(time_filter,limit=limit)

    post_lists=[]

    print(posts)
    # for post in posts:


def extract_posts_public(api:str,limit:None):

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    # Add limit parameter to URL if provided
    params = {}
    if limit:
        params['limit'] = limit
    
    try:
        response = requests.get(api, headers=headers, params=params)
        response.raise_for_status()  # Raises exception for 4xx/5xx status codes
        
        # Fix: Use .json() instead of .data
        data = response.json()
        print(f"Successfully retrieved {len(data.get('data', {}).get('children', []))} posts")
        print(data)
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Reddit: {e}")
        return None
