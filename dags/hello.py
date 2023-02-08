from datetime import timedelta, datetime

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago # handy scheduling tool


def print_date():
    """A very simple python function to call"""
    print(datetime.now())

# We can pass in DAG arguments using a default args dict. All these could be passed directly to the DAG as well.
default_args = {
    'start_date': days_ago(2), # The start date for DAG running. This function allows us to set the start date to two days ago
    'schedule_interval': timedelta(days=1), # How often our DAG will run. After the start_date, airflow waits for the schedule_interval to pass then triggers the DAG run
    'retries': 1, # How many times to retry in case of failure
    'retry_delay': timedelta(minutes=5), # How long to wait before retrying
}

# instantiate a DAG!
with DAG(
    'hello', # a unique name for our DAG
    description='A simple DAG to print "Hello World"', # a description of our DAG
    default_args=default_args, # pass in the default args.
) as dag:
    
    # create simple tasks:
    dummy_task = DummyOperator(
        task_id='dummy'
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
    hello_task >> [date_task, dummy_task]
