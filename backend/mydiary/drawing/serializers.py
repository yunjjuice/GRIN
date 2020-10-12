from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import Picture

class PictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Picture
        fields = ("image",)
