from django.urls import path

from app.users.api import api_v1

urlpatterns = [
    path("info", api_v1.UserInfoApi.as_view(), name="user information"),
]
