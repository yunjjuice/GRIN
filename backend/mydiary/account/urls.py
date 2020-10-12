from django.urls import path, include
from .views import *

urlpatterns = [
    path("", Register.as_view()),
    path("login/", Login.as_view()),
    path("user/", User.as_view()),
    path("<int:pk>/", ProfileAPIView.as_view()),
]