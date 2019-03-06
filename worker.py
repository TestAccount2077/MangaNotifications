import os, django
os.environ['DJANGO_SETTINGS_MODULE'] = 'MangaNotifications.settings'
django.setup()

from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from main.scheduled_events import *

print('Starting scheduler...')
scheduler = BlockingScheduler()

@scheduler.scheduled_job('interval', minutes=1)
def scheduled_job():
    
    dispatch_notifications()

scheduler.start()
