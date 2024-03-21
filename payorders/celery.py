import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'payorders.settings')

app = Celery('payorders', broker='amqp://admin:Suit1234@192.168.28.136:5672')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)