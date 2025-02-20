from random import randint
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EmailVerification
from .serializers import EmailVerificationSerializer
from rest_framework import status
from django.core.mail import send_mail
from root.settings import EMAIL_HOST_USER


@api_view(['POST'])
def send_code(request):
    serializer = EmailVerificationSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data["email"]
        code = randint(100000, 999999)
        EmailVerification.objects.create(email=email, code=code)

        subject = 'Verification Code'
        message = 'Your verification code is: {}'.format(code)
        email = serializer.validated_data["email"]
        recipient_list = [email]
        send_mail(subject, message, EMAIL_HOST_USER, recipient_list, fail_silently=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)