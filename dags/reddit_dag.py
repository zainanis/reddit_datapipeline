from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pipelines.reddit_pipeline_v02 import reddit_pipeline_v02


default_args ={
    'owner':'Zain Anis',
    'start_date':datetime(2025,11,11),
    'retries':5,
}

file_postfix=datetime.now().strftime("%Y%m%d")



dag=DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
    tags=['reddit','etl','pipeline']
)

extract = PythonOperator(
    task_id="reddit_extraction",
    python_callable=reddit_pipeline_v02,
    op_kwargs={
        'file_name':f'reddit_{file_postfix}',
        'subreddit':'dataenginering',
        'time_filter':'day',
        'limit':100
    },
    dag=dag

)


