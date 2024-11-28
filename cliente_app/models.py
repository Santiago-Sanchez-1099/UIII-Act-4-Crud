from django.db import models

class Cliente(models.Model):
    id_cliente = models.CharField(primary_key=True, max_length=11)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=128)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
