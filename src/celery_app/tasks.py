import time
from time import sleep
from celery import current_task
from .worker import celery_app

@celery_app.task
def add(x, y):
    for i in range(5):
        time.sleep(1)
        print(i)
    return x+y


@celery_app.task(acks_late=True)
def greeting(word: str) -> str:
    for i in range(1, 11):
        sleep(1)
        current_task.update_state(state='PROGRESS',
                                  meta={'process_percent': i*10})
    return f"Hello {word}"