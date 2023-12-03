from django.db import models

# Create your models here.

class usuario(models.Model):
    ID = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    tarjeta_o_cedula = models.CharField(max_length=50)
    Nombre_De_Ex = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre + " " + self.apellido
