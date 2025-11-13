import configparser
import os

parser = configparser.ConfigParser()


config_path = os.path.join(os.path.dirname(__file__), '../config/config.cfg')
parser.read(config_path)


# SECRET=parser.get('api_keys','reddit_secret_key')
# CLIENT_ID=parser.get('api_keys','reddit_client_id')
REDDIT_SUBREDDIT_PATH=parser.get('api','reddit_subreddit_path')

DATABASE_HOST =  parser.get('database', 'database_host')
DATABASE_NAME =  parser.get('database', 'database_name')
DATABASE_PORT =  parser.get('database', 'database_port')
DATABASE_USER =  parser.get('database', 'database_username')
DATABASE_PASSWORD =  parser.get('database', 'database_password')

# AWS_ACCESS_KEY_ID = parser.get('aws', 'aws_access_key_id')
# AWS_ACCESS_KEY = parser.get('aws', 'aws_secret_access_key')
# AWS_REGION = parser.get('aws', 'aws_region')
# AWS_BUCKET_NAME = parser.get('aws', 'aws_bucket_name')

INPUT_PATH = parser.get('file_paths', 'input_path')
OUTPUT_PATH = parser.get('file_paths', 'output_path')