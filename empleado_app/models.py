from django.db import models
class Empleado(models.Model):
    id_empleado = models.CharField(primary_key=True, max_length=11)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)  # Utiliza EmailField para validar correos automáticamente.
    password = models.CharField(max_length=128)  # Longitud recomendada para contraseñas encriptadas.
    puesto = models.CharField(max_length=20)
    fecha_registro = models.DateField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
