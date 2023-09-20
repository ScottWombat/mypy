from celery import Celery
import os
from core.config import config

celery_app = Celery(__name__)
celery_app.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://redis_broker:6379")
celery_app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis_broker:6379")

celery_app.conf.task_routes = {
    "celery_app.tasks.add": "add-queue",
    "celery_app.tasks.greeting": "greeting-queue",
}

# Optional configuration, see the application user guide.
celery_app.conf.update(
    result_expires=3600,
    task_track_started=True,
    broker_connection_retry_on_startup=True
)






