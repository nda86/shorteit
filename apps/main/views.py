from django.views import generic
from django.views import View
from .forms import ShortUrlCreateForm
from .services import create_short_url, get_list_url
from .models import ShortUrl
from django.shortcuts import redirect
from .models import ShortUrl


class HomeView(generic.TemplateView):
	template_name = "main/index.html"


class ShortUrlList(generic.ListView):
	context_object_name = 'links'
	template_name = "main/short_url_list.html"
	queryset = ShortUrl.objects.all()


class ShortUrlCreate(generic.FormView):
	form_class = ShortUrlCreateForm
	template_name = "main/short_url_create.html"

	def post(self, request, *args, **kwargs):
		short_url, created = create_short_url(request)
		return redirect('/')