from django.shortcuts import render, get_object_or_404
from .models import Pedido
from .forms import PedidoForm


# Create your views here.
def consultar_pedidos(request):
    return render(request,'pedidos.html')

def ver_pedido(request,pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    print(pedido.repartidor.id)
    print(pedido.repartidor.nombre)
    return render(request, 'ver_pedido.html', {'pedido':pedido})