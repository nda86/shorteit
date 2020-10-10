from rest_framework.serializers import ModelSerializer, CharField
from main.models import ShortUrl


class ShortUrlSerializer(ModelSerializer):
	class Meta:
		model = ShortUrl
		fields = '__all__'
