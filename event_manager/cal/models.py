from django.db import models

# Create your models here.
class Event(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    fecha = models.DateTimeField()
    dia = models.CharField(max_length=50)
    hora_inicio = models.DateTimeField()
    hora_fin = models.DateTimeField()
    grupo = models.CharField(max_length=50)
    profesor = models.CharField(max_length=50)