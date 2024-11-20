from django.shortcuts import render,redirect
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from .models import Carrito
from Usuario_app.models import Usuario
from Producto_app.models import Producto
from Pedido_app.models import Pedido, lista_de_pedidos
from Pedido_app.forms import PedidoForm


def agregar_a_carrito(request,producto_id):
    id = request.session['usuario_id']
    try:
        producto = Producto.objects.get(id=producto_id)
        if producto.stock == 0:
            messages.info(request,"Lo sentimos, no hay stock")
            return redirect('ver_catalogo',catalogo_id = producto.catalogo)
        else:
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
    total = carrito.aggregate(Sum('precio'))
    return render(request, 'carrito.html',{'carrito':carrito,'total':total['precio__sum']})

def aumentar_cantidad(request,pedido_carrito_id):
    id = request.session['usuario_id']
    try:
        carrito = Carrito.objects.get(id = pedido_carrito_id)
        producto = Producto.objects.get(id = carrito.id_producto.id)
        if producto.stock <= carrito.cantidad:
            messages.warning(request,"No hay mas stock del producto")
        else:
            carrito.cantidad += 1
            carrito.precio = carrito.id_producto.precio * carrito.cantidad
            producto.save()
            carrito.save()
    except Carrito.DoesNotExist:
        print("no existe")
    return redirect('mi_carrito',usuario_id = id)

def disminuir_cantidad(request,pedido_carrito_id):
    id = request.session['usuario_id']
    try:
        carrito = Carrito.objects.get(id = pedido_carrito_id)
        producto = Producto.objects.get(id = carrito.id_producto.id)

        if carrito.cantidad <= 1:
            producto.stock += 1
            carrito.delete()
            producto.save()
        else:
            producto.stock += 1
            carrito.cantidad -= 1
            producto.save()
            carrito.precio = carrito.id_producto.precio * carrito.cantidad
            carrito.save()
    except Carrito.DoesNotExist:
        print("no existe")
    return redirect('mi_carrito',usuario_id = id)    

def realizar_pedido(request):
    id = request.session['usuario_id']
    carrito = Carrito.objects.filter(id_usuario = id)
    form = PedidoForm()
    if request.method == "POST":
        print(request.POST)
        if form.is_valid:
            if pedir(request,data = {'direccion':request.POST['direccion']}):
                return redirect('pago exitoso')
            else:
                return redirect('pago fracaso')
    return render(request,'realizar_pedido.html',{'form':form})

def pedir(request,data):
    print("se esta generando el pedido")
    id = request.session['usuario_id']
    carrito = Carrito.objects.filter(id_usuario = id)
    pedido = Pedido.objects.filter(usuario_id = Usuario.objects.get(id = id),estado = 'activo')
    if Pedido.objects.filter(usuario_id = Usuario.objects.get(id = id),estado = 'activo'):
        for ped in Pedido.objects.filter(usuario_id = Usuario.objects.get(id = id),estado = 'activo'):
            print(ped)
        print(pedido)
        return False
    else:
        pre_pedido = Pedido()
        pre_pedido.repartidor = Usuario.objects.get(id = 2)
        pre_pedido.usuario = Usuario.objects.get(id = id)
        pre_pedido.estado = "activo"
        pre_pedido.fechaentrega = timezone.now()
        pre_pedido.descuento = 0.0
        pre_pedido.direccion = data["direccion"]
        print(carrito.aggregate(Sum('precio')))
        pre_pedido.total = carrito.aggregate(Sum('precio'))['precio__sum']
        pre_pedido.save()
        for car in carrito:
            lista = lista_de_pedidos()
            lista.id_pedido = pre_pedido
            lista.id_producto = car.id_producto
            producto = Producto.objects.get(id = car.id_producto.id)
            producto.stock -= car.cantidad
            if producto.stock <= 0:
                producto.estado = 'Desactivado'
            producto.save()
            lista.cantidad = car.cantidad
            lista.save()
        print("Se termino y guardo el pedido")
        carrito.delete()
        return True

def pagoexitoso(request):
    id = request.session['usuario_id']
    pedido = Pedido.objects.get(usuario = id, estado = 'activo')
    return render(request,"pagoexitoso.html",{'pedido':pedido}) 

def pagofracaso(request):
    return render(request,"pagofracaso.html")