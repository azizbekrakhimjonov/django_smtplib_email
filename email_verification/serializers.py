from rest_framework import serializers
from .models import EmailVerification

class EmailVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailVerification
        fields = ['email']