import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myhome24.settings')
app = Celery('myhome24')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
