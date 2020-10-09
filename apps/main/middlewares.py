import uuid
import logging


log = logging.getLogger("unhandled_exception")


class SetUserIdMiddleware:
	"""middleware для добавления в сессию идентификатора пользователя"""

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		user_id = str(uuid.uuid4())
		request.session.setdefault("user_id", user_id)
		response = self.get_response(request)
		return response


class CatchUnhadledException:
	"""middleware для обработки необработанных исключений"""

	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)
		return response

	def process_exception(self, request, exception):
		log.error("Произошло необработанное исключение!")
		log.error(exception, exc_info=True)
