from __future__ import absolute_import
import os
import time
import sched

from celery import Celery
from django.conf import settings

os.environ.setdefault( "DJANGO_SETTINGS_MODULE", "tweetSchedule.settings" )

app = Celery( "tweetSchedule" )
app.config_from_object( "django.conf:settings" )
app.autodiscover_tasks( settings.INSTALLED_APPS, related_name="tasks" )

print( "loaded" )

scheduler = sched.scheduler( time.time, time.sleep )
scheduler.run()

app.conf.update(
	CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend',
	BROKER_URL = 'redis://localhost:6379/0',
)

@app.task( bind=True )
def debug_task( self ):
	print( "Request: {0!r}".format( self.request ) )
