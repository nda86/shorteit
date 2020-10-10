import hashlib
import logging
from typing import Tuple
from django.http.request import HttpRequest
from django.db.models import QuerySet

from main.models import ShortUrl
from shorteit.settings import BASE_URL

# получаем объект логгера
log = logging.getLogger("debug_log")


def get_user_id(request: HttpRequest) -> str:
	"""Получение ид пользователя из сессии
	ид - это строковое представление uuid
	ид пользователя автоматически был помещен в сессию при первом заходе пользователя на сайт
	работу по добавлению ид пользователя в сессию выполняет SetUserIdMiddleware"""

	try:
		user_id = request.session.get("user_id")
		log.debug(f"Из запроса получен {user_id}")
		return user_id
	except Exception as e:
		log.error("Ошибка при получение user_id")
		log.error(e, exc_info=True)
		return ""


def gen_short_url(original_url: str) -> str:
	"""Cоздание subpart части для короткого url
	на основе введенного url гененируем <subpart> часть сокращенного url
	из ввееденного url генерируем хэш по алгоритму sha1, затем берем первые 10 символов из hex представления
	полученного хэша
	"""

	subpart = hashlib.sha1(original_url.encode()).hexdigest()[:10]
	log.debug(f"Сгенерирован <subpart> для короткого url {subpart}")
	return subpart


def create_short_url(request: HttpRequest) -> Tuple[bool, str]:
	"""Cоздание короткого url
	user_id - идентификатор пользователя,
	original_url - url адрес для которого нужно сделать короткий url. Вводится пользователем в форме на сайте
	subpart - url-path, часть короткого url в схеме <domain>\<subpart>. Может быть введена пользователем в форме
	на сайте. Если пользователь не заполнил это поле, то subpart генерируется приложением.
	short_url - короткий url для original_url. <domain>\<subpart>
	"""

	user_id = get_user_id(request)
	original_url = request.POST.get('original_url')
	subpart = request.POST.get('subpart').strip()
	if subpart:
		log.debug(f"Использован {subpart} введенный пользователем")
	short_url = BASE_URL + "/s/" + (subpart if subpart else gen_short_url(original_url))

	# обработка случая когда введенное пользователем subpart часть url уже использована
	if ShortUrl.objects.filter(short_url=short_url).first():
		log.warning(f"Ошибка при добавлении короткого url в бд. Сгенерированный url: {short_url} уже существует")
		return False, "Введенное сокращенное имя уже использовано. Введите другое или оставьте поле пустым!"

	# обработка случая когда пользователь пытается сократитиь уже сокращенный ранее адрес
	if ShortUrl.objects.filter(user_id=user_id, original_url=original_url).first():
		log.warning(f"Ошибка при добавлении короткого url в бд. Для {original_url} user уже создавал короткий url")
		return False, "Вы уже добавляли данный адрес. Введите другой адрес!"

	try:
		ShortUrl.objects.create(
			user_id=user_id,
			original_url=original_url,
			short_url=short_url
		)
		return True, f"Адрес {original_url} успешно сокращен"
	except Exception as e:
		log.error("Произошла ошибка при добавлении сгенерированного короткого url  в бд")
		log.error(e, exc_info=True)
		return False, "Неизвестная ошибка. Попробуйте повторить"


def get_queryset_short_url(request: HttpRequest) -> QuerySet:
	"""Получение списка объектов short_url из бд для отображения в шаблоне списка коротких url"""

	qs = ShortUrl.objects.filter(user_id=get_user_id(request)).all()
	log.debug("Из бд получен QuerySet")
	return qs


def get_original_url(short: str) -> ShortUrl:
	"""Получение из бд оригинального url по его короткому url
	Для выполнения редиректа пользователя
	(При заходе на короткий URL приложение редиректит на соответствующий ему URL
	"""

	original_url = ShortUrl.objects.filter(short_url=BASE_URL + "/s/" + short).first()
	log.debug(f"Из бд для subpart {short} был получен url: {original_url}")
	return original_url


def increment_count_links(url: ShortUrl) -> None:
	"""Инкремент счетчика переходов по ссылке
	При каждом переходе пользователя по короткому url, счетчик переходов этого корогтгоко url увеличиваем на 1.
	"""

	try:
		url.count_click += 1
		url.save()
		log.debug(f"Увеличен на 1 счетчик переходов по ссылке {url}")
	except Exception as e:
		log.error(f"Произошла ошибка при инкрименте счетчика переходов по ссылке {url}")
		log.error(e, exc_info=True)
