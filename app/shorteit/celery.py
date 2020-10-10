import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shorteit.settings')

app = Celery('shorteit')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
