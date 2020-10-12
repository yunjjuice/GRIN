from django.urls import path
from .views import *

urlpatterns = [
    path("extract/", ExtractAPIView.as_view()),
    path("emo/", EmoAPIView.as_view()),
]