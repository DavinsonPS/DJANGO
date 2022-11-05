from django.db import models

# Create your models here.
class Persona(models.Model):
    cedula = models.IntegerField(primary_key = True,null = False)
    nombre = models.CharField(max_length=50,null = False)
    apellido = models.CharField(max_length=50,null =False)

class Mascota(models.Model):
    id = models.AutoField(primary_key = True)
    dueno = models.ForeignKey(Persona, null = False, on_delete = models.CASCADE)
    nombre = models.CharField(max_length=50, null = False)
    raza = models.CharField(max_length=50, null = False)