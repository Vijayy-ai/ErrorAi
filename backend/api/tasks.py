# backend/api/tasks.py
from celery import shared_task
from services import unified_model

@shared_task
def process_user_input(user_input):
    return unified_model.process_input(user_input)

