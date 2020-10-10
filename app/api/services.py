import uuid
import logging
from main.models import ShortUrl
from main.services import gen_subpart
from shorteit.settings import BASE_URL


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


def gen_short_url(original_url, subpart):
	if subpart:
		log.debug(f"Короткий url будет создан с помощью пользовательского subpart {subpart}")
	subpart = subpart or gen_subpart(original_url)
	short_url = BASE_URL + "/s/" + subpart
	log.debug(f"Сгенерирован коротки url {short_url}")
	return short_url
