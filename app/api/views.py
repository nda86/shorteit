from rest_framework.viewsets import ModelViewSet

from .services import get_queryset_short_url
from .serializers import ShortUrlSerializer


class ShortUrlApi(ModelViewSet):
	queryset = get_queryset_short_url()
	serializer_class = ShortUrlSerializer
