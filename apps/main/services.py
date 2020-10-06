import hashlib
from django.http import HttpRequest
from .models import ShortUrl


def get_user_id(request):
	return request.session.get("user_id")


def gen_short_url(original_url):
	return hashlib.sha1(original_url.encode()).hexdigest()[:10]


def create_short_url(request):
	user_id = get_user_id(request)
	original_url = request.POST.get("original_url")
	short_url = gen_short_url(original_url)
	return ShortUrl.objects.get_or_create(defaults={
		'user_id': user_id,
		'original_url': original_url,
		'short_url': short_url},
		original_url=original_url, user_id=user_id
	)


def get_list_url():
	return ShortUrl.objects.filter(user_id=get_user_id()).all()