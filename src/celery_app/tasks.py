import time
from .worker import celery_app

@celery_app.task
def test_celery(x, y):
    for i in range(5):
        time.sleep(1)
        print(i)
    return x+y
