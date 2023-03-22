from django.db import models
from django.utils import timezone
# Create your models here.
class timeReader(models.Model):
    addDate = models.DateTimeField(default=timezone.now)
    timeReadedmilsec = models.PositiveIntegerField(default=0)
    timeReadedsecond = models.PositiveIntegerField(default=0)
    timeReadedminute = models.PositiveIntegerField(default=0)