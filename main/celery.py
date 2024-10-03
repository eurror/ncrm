from __future__ import absolute_import
from celery.schedules import crontab
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'main.settings')


app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-daily-report-every-morning': {
        'task': 'tasks.tasks.send_daily_report',
        'schedule': crontab(hour=7, minute=0),  # каждый день в 7 утра
    },
}
