from django.urls import path
from .views import HomeView, ShortUrlList, ShortUrlCreate


urlpatterns = [
	path('', HomeView.as_view(), name='home_view'),
	path('shorturl', ShortUrlList.as_view(), name='shorturl_list_view'),
	path('add', ShortUrlCreate.as_view(), name='shorturl_create_view'),
]
