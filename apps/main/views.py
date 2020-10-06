from django.views import generic
from django.views import View
from .forms import ShortUrlCreateForm
from .services import create_short_url, get_list_url
from .models import ShortUrl
from django.shortcuts import redirect
from .models import ShortUrl
from django.shortcuts import render
from django.contrib import messages


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
