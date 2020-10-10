from rest_framework.serializers import ModelSerializer
from app.apps.main.models import ShortUrl


class ShortUrlSerializer(ModelSerializer):
	class Meta:
		model = ShortUrl
		fields = '__all__'
