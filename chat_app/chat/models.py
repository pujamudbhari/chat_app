from datetime import datetime
from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    name = models.CharField(max_length=1000000)
    date = models.DateField(default=datetime.now, blank=True)
    room= models.CharField(max_length= 1000000)
    user= models.CharField(max_length= 10000000)

