from datetime import timedelta, datetime

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


def print_date():
    """A very simple python function to call"""
    print(datetime.now())


# instantiate a DAG!
with DAG(
    dag_id='01_hello',                      # a unique name for our DAG
    description='Hello World DAG',          # a description of our DAG
    start_date=datetime.utcnow(),           # when to start running this DAG
    schedule_interval=timedelta(days=1),    # how often to run this DAG
    catchup=False,                          # do NOT catch up on previously skipped tasks
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
