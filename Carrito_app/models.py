from django.db import models
from Producto_app.models import Producto
from Usuario_app.models import Usuario

# Create your models here.
class Carrito(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="carrito")
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name="en_carrito")
    cantidad = models.IntegerField()