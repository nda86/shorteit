import uuid


class SetUserIdMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		user_id = str(uuid.uuid4())
		request.session.setdefault("user_id", user_id)
		response = self.get_response(request)
		return response
