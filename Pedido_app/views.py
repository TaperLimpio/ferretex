from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from datetime import datetime
from .models import Pedido, lista_de_pedidos
from .forms import FiltroPedido,FiltroPedidoUsuario
from Usuario_app.models import Usuario


# Create your views here.
def consultar_pedidos(request):
    filtro = FiltroPedido()
    if request.method == "POST":
        filtro = FiltroPedido(request.POST)
        if filtro.is_valid():
            print(filtro.fields)
            estado = filtro.cleaned_data['estado']
            por_fecha = filtro.cleaned_data['filtra_por_fechar']
            fecha_de_inicio = filtro.cleaned_data['fecha_de_inicio']
            print(fecha_de_inicio)
            fecha_de_limite = filtro.cleaned_data['fecha_de_limite']
            print(fecha_de_limite)
            if por_fecha:
                pedidos = Pedido.objects.filter(fechainicio__range = [fecha_de_inicio,fecha_de_limite],
                                                fechaentrega__range = [fecha_de_inicio,fecha_de_limite])  
            elif (estado == 'Todo'):
                pedidos = Pedido.objects.all()
                print(pedidos)
            else:
                pedidos = Pedido.objects.filter(estado = estado)
    else:
        pedidos = Pedido.objects.all()
    print(pedidos)
    data = {'pedidos':pedidos,'form':filtro}
    return render(request,'pedidos.html',data)

def actualizar_pedido(request,id_pedido):
    pedido = Pedido.objects.get(id = id_pedido)
    data = {'direccion':pedido.direccion}
    if request.method == "POST":
        pedido.direccion = request.POST["txt_direccion"]
        pedido.save()
        return redirect('mis_pedidos')
    else:
        return render(request,'editar_pedido.html',data)

def ver_pedido(request,pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    lista_productos = lista_de_pedidos.objects.filter(id_pedido = pedido.id)
    return render(request, 'ver_pedido.html', {'pedido':pedido,'lista_productos':lista_productos})

def mis_pedidos(request):
    usuario_id = request.session['usuario_id']
    pedidos_activos = Pedido.objects.filter(
        Q(usuario = Usuario.objects.get(id=usuario_id)) & (Q(estado = 'activo') | Q(estado = 'tomado')))
    print(pedidos_activos)
        # estado = "activo",usuario = Usuario.objects.get(id=usuario_id)
    pedidos_pasados = Pedido.objects.filter(
        Q(usuario = Usuario.objects.get(id=usuario_id)) & Q(estado = "inactivo") | Q(estado = 'entregado'))

    filtro = FiltroPedidoUsuario()
    if request.method == "POST":
        filtro = FiltroPedidoUsuario(request.POST)
        if filtro.is_valid():
            print(filtro.fields)
            por_fecha = filtro.cleaned_data['filtra_por_fechar']
            fecha_de_inicio = filtro.cleaned_data['fecha_de_inicio']
            print(fecha_de_inicio)
            fecha_de_limite = filtro.cleaned_data['fecha_de_limite']
            print(fecha_de_limite)
            if por_fecha:
                """
                print(pedidos_activos.filter(fechainicio__range = [fecha_de_inicio,fecha_de_limite],
                                            fechaentrega__range = [fecha_de_inicio,fecha_de_limite]))
                print(pedidos_pasados.filter(fechainicio__range = [fecha_de_inicio,fecha_de_limite],
                                            fechaentrega__range = [fecha_de_inicio,fecha_de_limite]))
                """
                
                pedidos_activos_filtrados = pedidos_activos.filter(fechainicio__range = [fecha_de_inicio,fecha_de_limite],
                                                         fechaentrega__range = [fecha_de_inicio,fecha_de_limite]) 
                pedidos_pasados_filtrados = pedidos_pasados.filter(fechainicio__range = [fecha_de_inicio,fecha_de_limite],
                                                         fechaentrega__range = [fecha_de_inicio,fecha_de_limite])
                print(pedidos_activos_filtrados)
                print(pedidos_pasados_filtrados)
                return render(request,'mis_pedidos.html',{'ped_activos':pedidos_activos_filtrados,
                                              'ped_pasados':pedidos_pasados_filtrados,'form':filtro})
            
    return render(request,'mis_pedidos.html',{'ped_activos':pedidos_activos,
                                              'ped_pasados':pedidos_pasados,'form':filtro})     
                

    

def cancelar_pedido(request,id_pedido):
    pedido_tomado = Pedido.objects.get(id = id_pedido)
    pedido_tomado.estado = 'inactivo'
    pedido_tomado.save()
    return redirect('mis_pedidos')