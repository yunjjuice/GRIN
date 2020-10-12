from django.db import models

# Create your models here.
class Picture(models.Model):

    image = models.ImageField(upload_to="images/%Y/%m/%d", blank=True)
   
