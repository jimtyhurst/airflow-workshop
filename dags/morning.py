from datetime import timedelta, datetime

from airflow import DAG

from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago 


def brush_teeth():
    """A very simple python function to call"""
    print(f"calling brush_teeth function")

def toast_bread():
    """A very simple python function to call"""
    print(f"calling toast_bread function")

def butter_toast():
    """A very simple python function to call"""
    print(f"calling butter_toast function")

default_args = {
    'start_date': days_ago(2), 
    'schedule_interval': timedelta(days=1), 
    'retries': 1, 
    'retry_delay': timedelta(minutes=5), 
}

with DAG(
    'morning',
    description='A simple DAG for our morning routine',
    default_args=default_args, 
) as dag:

    alarm_task = BashOperator(
        task_id='alarm',
        bash_command='echo "RIIIINGGG" ',
    )

    snooze_task = BashOperator(
        task_id='snooze',
        bash_command='echo "snoozing" && sleep 4',
    )

    alarm_task2 = BashOperator(
        task_id='alarm2',
        bash_command='echo "RIIIINGGG" ',
    )

    # Define the tasks for brushing teeth, toasting bread, and buttering toast here
    # They'll be PythonOperators:

    # Set the task order here:
    
