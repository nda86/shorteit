from django.urls import path, include

from .views import ShortUrlApi
from rest_framework.routers import DefaultRouter


class OptionalSlashDefaulRouter(DefaultRouter):
	def __init__(self):
		super().__init__()
		self.trailing_slash = '/?'


router = OptionalSlashDefaulRouter()
router.register(r'shorturls', ShortUrlApi, basename='x')

urlpatterns = [
	path('', include(router.urls))
]
