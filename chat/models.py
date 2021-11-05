from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=50)

class Message(models.Model):
    value = models.CharField(max_length=1000)
    date = models.DateTimeField(default=datetime.now, blank=True)  #asignandole la libreria datetime para manejar la fecha de hoy
    user = models.CharField(max_length=50)
    room = models.CharField(max_length=100)
    