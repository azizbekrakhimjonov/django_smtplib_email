from django.urls import path
from .views import SendVerificationCode, VerifyCode

urlpatterns = [
    path('send/', SendVerificationCode.as_view(), name='send_code'),
    path('verify/', VerifyCode.as_view(), name='verify_code'),
]
