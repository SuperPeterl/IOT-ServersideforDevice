from django.db import models
from django.utils import timezone
# Create your models here.
class status(models.Model):
    addDate = models.DateTimeField(default=timezone.now)
    stid = models.CharField(default='',max_length=255)
    stdesc = models.CharField(default='',max_length=255)
    st = models.BooleanField(default= 0)
    listened = models.BooleanField(default=0)