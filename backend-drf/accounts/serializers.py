from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        # User.objects.create = saves the password in plain text
        # User.objects.create_user = automatically hashes the password

        # passing validated_data automatically
        # user = User.objects.create_user(**validated_data)     

        # passing validated_data manually
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'],
        )
        return user