import time
from time import sleep
from celery import current_task
from .worker import celery_app
import smtplib

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

@celery_app.task(acks_late=True)
def send_mail() -> str:
    s = smtplib.SMTP('smtp.gmail.com', 587)
 
    # start TLS for security
    s.starttls()
 
    # Authentication
    s.login("sender_email_id", "sender_email_id_password")
 
    # message to be sent
    message = "Message_you_need_to_send"
 
    # sending the mail
    s.sendmail("sender_email_id", "receiver_email_id", message)
 
    # terminating the session
    s.quit()
    return f"SUCCESS"