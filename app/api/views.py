import logging

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .services import get_queryset_short_url
from .serializers import ShortUrlSerializer
from .services import is_uuid


log = logging.getLogger('api_debug')


class ShortUrlApi(ModelViewSet):
	serializer_class = ShortUrlSerializer

	def get_queryset(self):
		return get_queryset_short_url(self.request)

	def create(self, request, *args, **kwargs):
		subpart = request.data.get("subpart")
		user_id = request.data.get("user_id")
		original_url = request.data.get("original_url")
		if not all([user_id, original_url]):
			log.warning("Не переданы все необходимые параметры (user_id, original_url)")
			return Response({'error': 'Both user_id and original_url required'})
		if not is_uuid(user_id):
			log.warning('user_id передан не в формате uuid')
			return Response({'error': 'user_id must be in uuid format'})
		create_short_url()