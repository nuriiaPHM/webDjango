from django.db import models

# Create your models here.

class Cliente(models.Model):
    dni = models.CharField(max_length=8)
    nombre = models.CharField(max_length=150)
    alta = models.DateTimeField('Fecha Alta')
