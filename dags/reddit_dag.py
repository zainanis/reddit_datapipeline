from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import sys


sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

default_args ={
    'owner':'Zain Anis',
    'start_date':datetime(2025,11,11)
}

file_postfix=datetime.now().strftime("%Y%m%d")

def test():
    print("Hello world")
    pass

dag=DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
    tags=['reddit','etl','pipeline']
)

extract = PythonOperator(
    task_id="reddit_extraction",
    python_callable=test,
    op_kwargs={
        'file_name':f'reddit_{file_postfix}',
        'subreddit':'dataenginering',
        'time_filter':'day',
        'limit':100
    }
)


