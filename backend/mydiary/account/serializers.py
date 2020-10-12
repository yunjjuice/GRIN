from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import User

# 회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], None, validated_data["password"]
        )
        return user


# 접속 유지중인지 확인(Authorization : token (토큰값))
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


# 로그인
class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials.")

# 프로필 정보
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','nickname','profilePic','intro','theme','birthdate')
        extra_kwargs = {'username': {'required': False}}
