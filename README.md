Account to access flower console
revit:rev123

Run application 

> poetry run python3 main.py  --env local --debug # run as a script
> poetry run python3 -m main --env local --debug # run as a module

Run Celery

>docker-compose exec worker1 python
>from celery_app.tasks import test_celery
>task = test_celery.delay(1,1)
>task.status
>task.result