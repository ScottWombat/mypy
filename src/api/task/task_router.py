import logging
import os
from fastapi import APIRouter, Response, Depends,  BackgroundTasks
from celery.result import AsyncResult
from pydantic import BaseModel

from core.fastapi.dependencies import PermissionDependency, AllowAll
from celery_app.worker import celery_app
from celery_app.tasks import greeting

class TaskOut(BaseModel):
    id: str
    status: str

log = logging.getLogger(__name__)

task_router = APIRouter()

@task_router.get("/start")
def start() -> TaskOut:
    r = greeting.delay("revit")
    return _to_task_out(r)


@task_router.get("/status/{task_id}")
def status(task_id: str) -> TaskOut:
    r = celery_app.AsyncResult(task_id)
    return _to_task_out(r)
    
def celery_on_message(body):
    log.warn(body)

def background_on_message(task):
    log.warn(task.get(on_message=celery_on_message, propagate=False))

@task_router.get("/send_task/{word}", dependencies=[Depends(PermissionDependency([AllowAll]))])
async def root(*,word: str, background_task: BackgroundTasks):
    task_name = "celery_app.tasks.greeting"
  
    task = celery_app.send_task(task_name, args=[word])
    print(task)
    background_task.add_task(background_on_message, task)

    return {"message": "Word received"}

def _to_task_out(r: AsyncResult) -> TaskOut:
    return TaskOut(id=r.task_id, status=r.status)
