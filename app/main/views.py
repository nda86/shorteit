import logging
from typing import Callable

from django.views import generic
from django.shortcuts import redirect
from django.contrib import messages
from django.http.request import HttpRequest

from .forms import ShortUrlCreateForm
from .services import (
	create_short_url, get_queryset_short_url, get_original_url, increment_count_links
)

# получаем объект логгера
log = logging.getLogger('debug_log')


class HomeView(generic.TemplateView):
	"""вьюха для главной страницы сайта"""

	template_name = "main/index.html"


class ShortUrlList(generic.ListView):
	"""вьюха для страницы со списком коротких url"""

	context_object_name = 'links'
	template_name = "main/short_url_list.html"
	paginate_by = 3

	def get_queryset(self):
		return get_queryset_short_url(self.request)


class ShortUrlCreate(generic.FormView):
	"""вьюха для страницы создания короткого url"""

	form_class = ShortUrlCreateForm
	template_name = "main/short_url_create.html"

	def post(self, request, *args, **kwargs):
		"""если в переменную success приходит False, то в переменной msg будет описание ошибки
		example: msg = "some error"
		если success=True, то в msg строка об успешной операции
		example: msg = "ok"
		"""

		success, msg = create_short_url(request)
		if not success:
			log.error(f"Ошибка при создании короткого url {msg}")
			messages.error(request, msg)
			return redirect("shorturl_create_view")

		log.debug(f"Короткий url успешно добавлен в бд")
		messages.info(request, msg)
		return redirect("shorturl_list_view")


def redirect_to_original_url(request: HttpRequest, short: str) -> Callable:
	"""фунцкция выполняет редирект на url по его короткому url"""

	url = get_original_url(short)
	if url:
		log.debug(f"Редирект на {url.original_url}")
		increment_count_links(url)
		return redirect(url.original_url)
	else:
		log.warning(f"Запрошенный короткий url c subpart '{short}' не был найден")
		messages.warning(request, "Запрошенный URL не найден. Возможно он уже удален из базы")
		return redirect('shorturl_list_view')
