from django.db import models

# Create your models here.

class Calificaciones(models.Model):
    grupo = models.CharField(max_length=100)
    nombre_profesor = models.CharField(max_length=100)
    nombre_materia = models.CharField(max_length=100)
    calificacion_1 = models.DecimalField(max_digits=10, decimal_places=2)
    calificacion_2 = models.DecimalField(max_digits=10, decimal_places=2)
    calificacion_3 = models.DecimalField(max_digits=10, decimal_places=2)
    evaluacion_final = models.DecimalField(max_digits=10, decimal_places=2)
    calificacion_final = models.DecimalField(max_digits=10, decimal_places=2)