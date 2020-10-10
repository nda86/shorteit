import logging

from rest_framework.viewsets import ModelViewSet

from .services import get_queryset_short_url
from .serializers import ShortUrlSerializer


log = logging.getLogger('api_debug')


class ShortUrlApi(ModelViewSet):
	serializer_class = ShortUrlSerializer

	def get_queryset(self):
		return get_queryset_short_url(self.request)
