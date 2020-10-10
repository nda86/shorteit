from django.urls import path, re_path, include


urlpatterns = [
    path('api/v1/', include("api.urls")),
    path('', include("main.urls")),
]
