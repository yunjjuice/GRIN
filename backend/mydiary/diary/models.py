from django.db import models
from django.utils import timezone
# Create your models here.
class Diary(models.Model):
    user = models.ForeignKey("account.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/diaryImg", blank=True)
    createdate = models.DateTimeField(default=timezone.now)
    font = models.IntegerField(default=1)
    emotion = models.IntegerField(default=1)
    
