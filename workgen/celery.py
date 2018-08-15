from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workgen.settings')

app = Celery('workgen')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.broker_transport_options = {'visibility_timeout': 3600}  # 1 hour
app.conf.result_backend = 'redis://localhost:6379/0'
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))