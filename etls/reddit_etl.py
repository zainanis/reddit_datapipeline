import praw
from praw import Reddit
import sys


def connect_reddit(client_id,client_secret,user_agent)->Reddit:
    try:
        reddit=Reddit(client_id,client_secret,user_agent)
        print("connected to reddit")
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)