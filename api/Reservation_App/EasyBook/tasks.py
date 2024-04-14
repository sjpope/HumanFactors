from celery import shared_task
from .models import *

@shared_task
def recommend_task(params):
    pass