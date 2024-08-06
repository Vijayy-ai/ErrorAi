# backend/error_ai/celery.py
# import os
# from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'error_ai.settings')

# app = Celery('error_ai')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()


#backend/error_ai/celery.py
import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'error_ai.settings')

app = Celery('error_ai')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')