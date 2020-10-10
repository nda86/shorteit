import uuid
import logging
from main.models import ShortUrl


log = logging.getLogger('api_debug')


def get_queryset_short_url(request):
	"""функция возвращает список shorturl конкретного пользователя"""
	user_id = request.query_params.get('user_id')
	try:
		qs = ShortUrl.objects.filter(user_id=user_id)
		return qs
	except Exception as e:
		# если случилась ошибка в бд, то клиенту просто отдаем пустой список, а ошибку логируем
		# в дальнейшем сделать отправку пользователю информативного сообщения
		log.error(f"Ошибка бд при запросе списка ссылок для юзера {user_id}")
		log.error(e, exc_info=True)
		return []


def is_uuid(s):
	# проверяем что s в формате uuid
	try:
		uuid.UUID(s, version=4)
		return True
	except ValueError as e:
		log.debug(f"Переданный параметр: {s} не в формате uuid!")
		return False
