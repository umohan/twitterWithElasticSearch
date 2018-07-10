from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class tweet(models.Model):
   id = models.TextField(primary_key=True,max_length=10000)
   created_at = models.DateTimeField( null=True, blank=True)
   text = models.CharField(max_length=20000)
   userId = models.TextField(max_length=1000)
