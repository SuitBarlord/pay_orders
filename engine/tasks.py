from celery import shared_task
from django.core.mail import send_mail
from .models import Reestr_oferts
import time


@shared_task
def order_created():
    procces = 'celery create'
    time.sleep(4)
    print('Celery')
    
    return procces