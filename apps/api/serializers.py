from rest_framework.serializers import ModelSerializer
from apps.main.models import ShortUrl


class ShortUrlSerializer(ModelSerializer):
	class Meta:
		model = ShortUrl
		fields = '__all__'
