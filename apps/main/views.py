from django.views import generic


class HomeView(generic.TemplateView):
	template_name = "main/index.html"


class ShortUrlView(generic.TemplateView):
	template_name = "main/short_url_list.html"
