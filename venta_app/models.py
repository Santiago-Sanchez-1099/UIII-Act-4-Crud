from django.db import models
class Venta(models.Model):
    id_venta = models.CharField(primary_key=True, max_length=11)
    fecha_venta = models.DateField()
    producto = models.CharField(max_length=50)
    cantidad = models.IntegerField(5)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=20)
    id_producto = models.CharField(max_length=11)
    id_empleado = models.CharField(max_length=11)
    id_cliente = models.CharField(max_length=11)

    def __str__(self):
        return self.id_venta
    
    #id_producto = models.CharField(primary_key=True, max_length=11)
    #nombre_producto = models.CharField(max_length=50)
    #descripcion = models.CharField(max_length=100)
    #stock = models.IntegerField()
    #precio = models.DecimalField(max_digits=10, decimal_places=2)
    #fecha_ingreso = models.DateField()
    #id_categoria = models.CharField(max_length=11)