from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from . import views

router = DefaultRouter()
router.register(r'',views.DiaryViewSet)
urlpatterns = [
    path("", include(router.urls)),
    # path("<int:pk>/", DiaryAPIView.as_view()),
]