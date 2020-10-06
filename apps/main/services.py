import hashlib
from .models import ShortUrl


def get_user_id(request):
	return request.session.get("user_id")


def gen_short_url(original_url):
	return hashlib.sha1(original_url.encode()).hexdigest()[:10]


def create_short_url(request):
	user_id = get_user_id(request)
	original_url = request.POST.get("original_url")
	subpart = request.POST.get("subpart").strip()
	short_url = subpart if subpart else gen_short_url(original_url)

	# обработка случая когда введенное пользователем subpart часть url уже использована
	if ShortUrl.objects.filter(short_url=short_url).first():
		return False, "Введенное сокращенное имя уже использовано. Введите другое или оставьте поле пустым!"

	# обработка случая когда пользователь пытается сократитиь уже сокращенный ранее адрес
	if ShortUrl.objects.filter(user_id=user_id, original_url=original_url).first():
		return False, "Вы уже добавляли данный адрес. Введите другой адрес!"

	try:
		ShortUrl.objects.create(
			user_id=user_id,
			original_url=original_url,
			short_url=short_url
		)
		return True, f"Адрес {original_url} успешно сокращен"
	except Exception as e:
		return False, "Неизвестная ошибка. Попробуйте повторить"


def get_list_url(request):
	return ShortUrl.objects.filter(user_id=get_user_id(request)).all()