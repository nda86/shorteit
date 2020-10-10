from rest_framework.serializers import ModelSerializer, CharField
from main.models import ShortUrl
from .services import gen_short_url


class ShortUrlSerializer(ModelSerializer):
	short_url = CharField(max_length=255, required=False)

	def save(self, **kwargs):
		original_url = self.validated_data.get("original_url")
		subpart = self.validated_data.get("short_url")
		self.validated_data["short_url"] = gen_short_url(original_url, subpart)
		super().save(**kwargs)

	class Meta:
		model = ShortUrl
		fields = '__all__'
