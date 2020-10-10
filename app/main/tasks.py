from datetime import date, timedelta

from celery import shared_task
from .models import ShortUrl


@shared_task(name='clear_shorturl')
def clear_shorturl():
	"""задача для celery по очистке записей старше 7 дней"""
	seven_days_ago = date.today() - timedelta(days=7)
	ShortUrl.objects.filter(created_at__lt=seven_days_ago).delete()
