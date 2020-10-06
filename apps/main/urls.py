from django.urls import path
from .views import HomeView, ShortUrlView


urlpatterns = [
	path('', HomeView.as_view(), name='home_view'),
	path('shorturl', ShortUrlView.as_view(), name='short_url_view')
]
