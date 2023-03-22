from django.db import models
from django.utils import timezone
# Create your models here.
class timeReader(models.Model):
    startdate = models.DateTimeField(default=timezone.now) 