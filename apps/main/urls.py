from django.urls import path, re_path
from .views import HomeView, ShortUrlList, ShortUrlCreate, redirect_to_original_url


urlpatterns = [
	path('', HomeView.as_view(), name='home_view'),
	path('shorturls', ShortUrlList.as_view(), name='shorturl_list_view'),
	path('add', ShortUrlCreate.as_view(), name='shorturl_create_view'),
	re_path(r'^(?P<short>.*)', redirect_to_original_url)
]
