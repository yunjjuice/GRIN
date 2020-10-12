from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Diary
from account.serializers import UserSerializer

class DiarySerializer(serializers.ModelSerializer):

    user = UserSerializer()
    class Meta:
        model = Diary
        fields = ("id", "user", "title", "content", "image", "createdate", "font", "emotion")
class DiarySaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ("id", "user", "title", "content", "image", "createdate", "font", "emotion")