from django.views import generic
from django.shortcuts import redirect
from django.contrib import messages

from .forms import ShortUrlCreateForm
from .services import (
	create_short_url, get_list_url, get_original_url, increment_count_links
)


class HomeView(generic.TemplateView):
	template_name = "main/index.html"


class ShortUrlList(generic.ListView):
	context_object_name = 'links'
	template_name = "main/short_url_list.html"

	def get_queryset(self):
		return get_list_url(self.request)


class ShortUrlCreate(generic.FormView):
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
			messages.error(request, msg)
			return redirect("shorturl_create_view")

		messages.info(request, msg)
		return redirect("shorturl_list_view")


def redirect_to_original_url(request, short):
	url = get_original_url(short)
	if url:
		increment_count_links(url)
		print(url.original_url)
		return redirect(url.original_url)
	else:
		messages.warning(request, "Запрошенный URL не найден. Возможно он уже удален из базы")
		return redirect('shorturl_list_view')
