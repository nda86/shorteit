from django.urls import path, re_path, include


urlpatterns = [
    path('api/v1/', include("app.apps.api.urls")),
    path('', include("app.apps.main.urls")),
]
