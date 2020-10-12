from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

# Create your views here.
class DiaryViewSet(viewsets.ModelViewSet):
    
    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    
    def get_queryset(self):
        user_id = self.request.query_params.get('user', None)
        if user_id is None:
            return Diary.objects.all()
        return Diary.objects.filter(user = user_id)

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PUT'):
            return DiarySaveSerializer
        return self.serializer_class

