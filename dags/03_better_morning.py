from datetime import timedelta, datetime
import random

from airflow.decorators import dag, task
from airflow.operators.bash import BashOperator


# **** DEFINING DAGS USING DECORATORS ****

# task decorator creates a PythonOperator
@task
def brush_teeth():
    """Brush your teeth"""
    print(f"calling brush_teeth function")

@task
def toast_bread():
    """Toast bread"""
    num_of_toast = random.randint(2, 5)
    print(f"toasting {num_of_toast} pieces of bread")
    return num_of_toast


@task
def butter_toast(num_toast: int = 2):
    """Butter up that bread"""
    print(f"buttering up {num_toast} pieces of bread")


# defining the DAG via @dag decorator
@dag(
    dag_id='better_morning',
    description='A simple DAG for our morning routine',
    start_date=datetime.utcnow(),           # when to start running this DAG
    is_paused_upon_creation=True,           # paused by default
)
def better_morning():
    """Morning routine DAG with decorators"""

    alarm_task = BashOperator(
        task_id='alarm',
        bash_command='echo "RIIIINGGG" ',
    )

    snooze_task = BashOperator(
        task_id='snooze',
        bash_command='echo "snoozing" && sleep 3',
    )

    alarm_task2 = BashOperator(
        task_id='alarm2',
        bash_command='echo "RIIIINGGG" ',
    )

    brush_task = brush_teeth()
    toast_task = toast_bread()
    butter_task = butter_toast(toast_task)


    # Set the task order here:
    alarm_task >> snooze_task >> alarm_task2 >> brush_task >> toast_task >> butter_task



# create the dag
dag = better_morning()
