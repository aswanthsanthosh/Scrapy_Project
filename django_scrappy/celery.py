# celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_scrappy.settings')

app = Celery('django_scrappy')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.task_default_queue = 'scraping'

app.conf.update(
    worker_concurrency=20,
    worker_prefetch_multiplier=1,  
)
