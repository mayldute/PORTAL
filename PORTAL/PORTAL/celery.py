import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PORTAL.settings')
 
app = Celery('PORTAL')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'weekly_notify': {
        'task': 'posts.tasks.weekly_notify',
        'schedule': crontab(),
    },
}