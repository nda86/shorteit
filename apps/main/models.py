from django.db import models


class ShortUrl(models.Model):
	"""модель основной таблицы в бд.
	Таблица сокращенных урлов. Содержит сведения о пользователе, оригинальный урл, дату создания, количество переходов
	по короткому урлу и собственно сам сокращенный урл.
	"""
	user_id = models.UUIDField(verbose_name="Идентификатор пользователя")
	original_url = models.URLField(verbose_name="Оригинальный URL", unique=True)
	short_url = models.URLField(verbose_name="Сокращенный URL")
	created_at = models.DateTimeField(verbose_name="Дата создания короткого URL", auto_now_add=True)
	count_click = models.IntegerField(verbose_name="Количество переходов по короткому URL", default=0)

	def __str__(self):
		return f"Short Url: {self.short_url}"

	class Meta:
		db_table = "main_short_url"
