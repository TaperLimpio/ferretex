from django.shortcuts import render,redirect
from django.db.models import Sum
from .models import Carrito
from Usuario_app.models import Usuario
from Producto_app.models import Producto
from Pedido_app.models import Pedido, lista_de_pedidos

def agregar_a_carrito(request,producto_id):
    id = request.session['usuario_id']
    try:
        carrito = Carrito.objects.get(id_producto = producto_id, id_usuario = id)
        carrito.cantidad += 1
        carrito.precio = carrito.id_producto.precio * carrito.cantidad
        carrito.save()
    except Carrito.DoesNotExist:
        carrito = Carrito()
        carrito.id_usuario = Usuario.objects.get(id=id)
        carrito.id_producto = Producto.objects.get(id=producto_id)
        carrito.cantidad = 1
        carrito.precio = carrito.id_producto.precio * carrito.cantidad
        carrito.save()
    return redirect('mi_carrito',usuario_id = id)


def ver_carrito(request,usuario_id):
    carrito = Carrito.objects.filter(id_usuario = usuario_id)
    total = Carrito.objects.aggregate(Sum('precio'))
    return render(request, 'carrito.html',{'carrito':carrito,'total':total['precio__sum']})

def aumentar_cantidad(request,pedido_carrito_id):
    id = request.session['usuario_id']
    try:
        carrito = Carrito.objects.get(id = pedido_carrito_id)
        carrito.cantidad += 1
        carrito.precio = carrito.id_producto.precio * carrito.cantidad
        carrito.save()
    except Carrito.DoesNotExist:
        print("no existe")
    return redirect('mi_carrito',usuario_id = id)

def disminuir_cantidad(request,pedido_carrito_id):
    id = request.session['usuario_id']
    try:
        carrito = Carrito.objects.get(id = pedido_carrito_id)
        if carrito.cantidad == 0:
            None
        else:
            carrito.cantidad -= 1
        carrito.precio = carrito.id_producto.precio * carrito.cantidad
        carrito.save()
    except Carrito.DoesNotExist:
        print("no existe")
    return redirect('mi_carrito',usuario_id = id)    

def realizar_pedido(request):
    id = request.session['usuario_id']
    pre_pedido = Pedido()
    carrito = Carrito.objects.filter(id_usuario = id)
    for car in carrito:
        print(car.precio)
    return redirect('mi_carrito',usuario_id = id)  