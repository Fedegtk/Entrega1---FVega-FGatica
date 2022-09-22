from django.db import models

# Create your models here.
class Curso(models.Model):
    materia = models.CharField(max_length=40)
    numero = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    area = models.CharField(max_length=30)