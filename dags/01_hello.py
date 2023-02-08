from datetime import timedelta, datetime

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago


def print_date():
    """A very simple python function to call"""
    print(datetime.now())


# instantiate a DAG!
with DAG(
    dag_id='hello',                         # a unique name for our DAG
    description='Hello World DAG',          # a description of our DAG
    start_date=days_ago(2),                 # when to start running this DAG
    schedule_interval=timedelta(days=1),    # how often to run this DAG
    catchup=False,                          # do NOT run previous unscheduled tasks
    is_paused_upon_creation=True,           # paused by default
) as dag:
    
    # create simple tasks:
    dummy_task = EmptyOperator(
        task_id='start'
    )

    hello_task = BashOperator(
        task_id='print_hello',
        bash_command='echo Hello World'
    )

    date_task = PythonOperator(
        task_id="date_task",
        python_callable=print_date
    )

    # set the task order
    dummy_task >> hello_task >> date_task
