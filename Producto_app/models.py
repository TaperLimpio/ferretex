from django.db import models
from Sucursal_app.models import Sucursal
from Catalogo_app.models import Catalogo

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='producto-imagenes/')
    sucursales = models.ManyToManyField(Sucursal, through='ProductoSucursal')
    catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE, related_name='productos_set')
    estado = models.CharField(max_length=20, default='Desactivado')

class ProductoSucursal(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    producto = models.ForeignKey('Producto_app.Producto', on_delete=models.CASCADE)
    disponibilidad = models.BooleanField(default=True)