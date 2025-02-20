# email_verification/urls.py
from django.urls import path
from .views import send_code

urlpatterns = [
    path("send/", send_code, name="send_code"),
]
