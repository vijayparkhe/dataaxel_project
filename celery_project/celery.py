from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

app = Celery('celery_project')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
#app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object(settings, namespace='CELERY')

#celery Beat settings
app.conf.beat_schedule = {
    'send_mail_every_birthday_dates':{
        'task': 'send_email.tasks.send_birthday_greetings',
        'schedule' : crontab(hour='0',minute='0'),
    }

}
# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

