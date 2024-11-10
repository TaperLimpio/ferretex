from django.shortcuts import render,redirect
from django.db.models import Sum
from .models import Carrito
from Usuario_app.models import Usuario
from Producto_app.models import Producto

def agregar_a_carrito(request,producto_id):
    id = request.session['usuario_id']
    carrito = Carrito()
    carrito.id_usuario = Usuario.objects.get(id=id)
    carrito.id_producto = Producto.objects.get(id=producto_id)
    carrito.save()
    return redirect(request,'pagina_principal/')

def ver_carrito(request,usuario_id):
    carrito = Carrito.objects.filter(id_usuario = usuario_id)
    total = Carrito.objects.values('id_producto__precio')
    return render(request, 'carrito.html',{'carrito':carrito,'total':total})