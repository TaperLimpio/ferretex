from django.shortcuts import render, redirect,get_object_or_404
from  PaginaWeb.models import Usuario  # Asegúrate de que esta sea tu clase de usuario
from Pedido_app.models import Pedido
from . import forms
from .forms import UsuarioForm,UsuarioAdminForm

# Create your views here.
def portalpago(request):
    return render(request,'portalpago.html')

def Administrador(request):
    return render(request, "pagina-admin.html")

def Repartidor(request):
    return render(request, "pagina-repartidor.html")

def ingresarproducto(request):
    return render(request,"ingresarproductos.html")

def verproducto(request):
    return render(request, 'verproducto.html')

def paginaprincipal(request):
    return render(request,"paginaprincipal.html")

