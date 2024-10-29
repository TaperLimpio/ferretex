from django.shortcuts import render

# Create your views here.
def portalpago(request):
    return render(request,'portalpago.html')

def Login(request):
    return render(request, "login.html")

def CrearCuenta(request):
    return render(request, "crear-cuenta.html")

def Administrador(request):
    return render(request, "pagina-admin.html")

def Repartidor(request):
    return render(request, "pagina-repartidor.html")

def CrearCuentaAdmin(request):
    return render(request, "crear-cuenta-admin.html")

def ingresarproducto(request):
    return render(request,"ingresarproducto.html")

def verproducto(request):
    return render(request, 'verproducto.html')

def pagofracaso(request):
    return render(request,"pagofracaso.html")

def pagoexitoso(request):
    return render(request,"pago exitoso.html")

def ingresarcatalogo(request):
    return render(request,"ingresar catalogo.html")

def paginaprincipal(request):
    return render(request,"paginaprincipal.html")

def ingresarlocal(request):
    return render(request,"ingresar local.html")

def carritocompra(request):
    return render(request,'carrito.html')
