from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from .models import CustomUser

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            is_active=True,
        )
        return user



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
