from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=10, blank=True)
    profilePic = models.ImageField(upload_to="images/profilePic", blank=True)
    intro = models.CharField(max_length=200, blank=True)
    theme = models.IntegerField(default=1)
    birthdate = models.DateTimeField(default=timezone.now)