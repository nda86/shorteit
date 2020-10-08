from django.urls import path, re_path, include


urlpatterns = [
    path('api/v1/', include("apps.api.urls")),
    path('', include("apps.main.urls")),
]
