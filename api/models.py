from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string
import re

def validate_curp(value):
    # Expresión regular para validar el formato del CURP
        curp_pattern = r"^[A-Z]{4}\d{6}[HM][A-Z]{5}\d{2}$"
        if not re.match(curp_pattern, value):
            raise ValidationError("El CURP ingresado no es válido.")

# Create your models here.

class Alumno(models.Model):
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=10, unique=True, blank=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    genero = models.CharField(choices=GENERO_CHOICES)
    curp = models.CharField(
        max_length=150,
        validators=[
            validate_curp,
        ],
    )
    def save(self, *args, **kwargs):
        if not self.matricula:
            self.matricula = get_random_string(length=10)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.matricula}"
    

class Profesores(models.Model):
     GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     matricula = models.CharField(max_length=10, unique=True, blank=True)
     email = models.EmailField(unique=True)
     nombre = models.CharField(max_length=100)
     apellido_paterno = models.CharField(max_length=100)
     apellido_materno = models.CharField(max_length=100)
     direccion = models.CharField(max_length=100)
     genero = models.CharField(choices=GENERO_CHOICES)
     curp = models.CharField(
          max_length=150,
          validators=[
               validate_curp
          ],
     )
     def save(self, *args, **kwargs):
        if not self.matricula:
            self.matricula = get_random_string(length=10)
        super().save(*args, **kwargs)
    
     def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.matricula}"


class Control(models.Model):
     GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    ]
     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     nombre = models.CharField(max_length=100)
     matricula = models.CharField(max_length=10, unique=True, blank=True)
     email = models.EmailField(unique=True)
     apellido_paterno = models.CharField(max_length=100)
     apellido_materno = models.CharField(max_length=100)
     direccion = models.CharField(max_length=100)
     genero = models.CharField(choices=GENERO_CHOICES)
     curp = models.CharField(
          max_length=150,
          validators=[
               validate_curp
          ],
     )
     def save(self, *args, **kwargs):
        if not self.matricula:
            self.matricula = get_random_string(length=10)
        super().save(*args, **kwargs)

     def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.matricula}"

class Calificaciones(models.Model):
    grupo = models.CharField(max_length=100)
    nombre_profesor = models.CharField(max_length=100)
    nombre_materia = models.CharField(max_length=100)
    calificacion_1 = models.DecimalField(max_digits=10, decimal_places=2)
    calificacion_2 = models.DecimalField(max_digits=10, decimal_places=2)
    calificacion_3 = models.DecimalField(max_digits=10, decimal_places=2)
    evaluacion_final = models.DecimalField(max_digits=10, decimal_places=2)
    calificacion_final = models.DecimalField(max_digits=10, decimal_places=2)    
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesores, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.grupo} - {self.nombre_profesor} - {self.nombre_materia}"

        