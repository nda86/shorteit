from main.models import ShortUrl


def get_queryset_short_url():
	return ShortUrl.objects.all()