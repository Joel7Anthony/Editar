from django.db import models

# Create your models here.
class Task(models.Model):
    modelo      = models.CharField(max_length=50)
    año         = models.CharField(max_length=50)
    placa       = models.CharField(max_length=50)
    chasis      = models.CharField(max_length=50)
    propietario = models.CharField(max_length=50)
    
