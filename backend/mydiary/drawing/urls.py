from django.urls import path, include
from .views import *

urlpatterns = [
    path("picture/", UploadAPIView.as_view()),
    path("keyword/", KeywordAPIView.as_view()),
]