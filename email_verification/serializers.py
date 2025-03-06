from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'verification_code', 'is_verified']
        read_only_fields = ['verification_code', 'is_verified']
