from django.shortcuts import render, redirect, get_object_or_404
from .forms import CatalogoForm
from .models import Catalogo
from Producto_app.models import Producto

def ingresarcatalogo(request):
    form = CatalogoForm()
    if request.method == 'POST':
        form = CatalogoForm(request.POST, request.FILES)  # Asegúrate de manejar archivos
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir a una URL después de guardar el formulario
    data = {'form': form, 'titulo': 'Agregar catálogo'}
    return render(request, 'ingresar_catalogo.html', data)


def paginaprincipal(request): 
    catalogos = Catalogo.objects.filter(estado='Activado').prefetch_related('producto_set').all() 
    return render(request, 'pagina_principal.html', {'catalogos': catalogos})


def paginaadmin(request):
    catalogos = Catalogo.objects.prefetch_related('producto_set').all()
    return render(request, 'pagina-admin.html', {'catalogos': catalogos})

def actualizarcatalogo(request, catalogo_id):
    catalogo = get_object_or_404(Catalogo, id=catalogo_id)
    if request.method == 'POST':
        form = CatalogoForm(request.POST, request.FILES, instance=catalogo)  # Vincula el formulario con el catálogo existente
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir a una URL después de actualizar el formulario
    else:
        form = CatalogoForm(instance=catalogo)
    data = {'form': form, 'titulo': 'Actualizar catálogo'}
    return render(request, 'ingresar_catalogo.html', data)



def asignar_producto(request, catalogo_id):
    catalogo = get_object_or_404(Catalogo, id=catalogo_id)
    productos = Producto.objects.filter(catalogo__isnull=True)  # solo platillos sin catálogo asignado
    if request.method == 'POST':
        productos_id = request.POST.get('producto_id')
        producto = get_object_or_404(Producto, id=productos_id)
        producto.catalogo = catalogo
        producto.save()
        return redirect('login')  # Redirige a la página de administración
    return render(request, 'asignar_producto.html', {'catalogo': catalogo, 'producto': productos})

def ver_catalogo(request, catalogo_id):
    catalogo = get_object_or_404(Catalogo, id=catalogo_id)
    productos_activados = catalogo.productos_set.filter(estado='Activado')
    return render(request, 'ver_catalogo.html', {'catalogo': catalogo, 'platillos': productos_activados})


def ver_catalogoadmin(request, catalogo_id):
    catalogo = get_object_or_404(Catalogo, id=catalogo_id)
    return render(request, 'ver_catalogo_admin.html', {'catalogo': catalogo})


def activar_catalogo(request, catalogo_id): 
    catalogo = get_object_or_404(Catalogo, id=catalogo_id) 
    catalogo.estado = 'Activado' 
    catalogo.save() 
    return redirect('pagina_administrador')

def desactivar_catalogo(request, catalogo_id):
    catalogo = get_object_or_404(Catalogo, id=catalogo_id)
    catalogo.estado = 'Desactivado'
    catalogo.save()
    return redirect('pagina_administrador')


