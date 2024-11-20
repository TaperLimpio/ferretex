from django.shortcuts import render, redirect,get_object_or_404
from .forms import ProductoForm,Producto,ProductoActualizarForm

def ingresarproducto(request):
    
    form = ProductoForm()
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)  # Asegúrate de manejar archivos
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir a una URL después de guardar el formulario
    data = {'form': form, 'titulo': 'Agregar catálogo'}
    return render(request, 'ingresar_catalogo.html', data)
    """
    if request.method == 'POST':
        formset = [ProductoForm(request.POST, request.FILES, prefix=str(i)) for i in range(3)]
        valid_forms = []
        any_errors = False
        
        for form in formset:
            if any(form.data.get(form.prefix + '-' + field, '') for field in form.fields):
                if form.is_valid():
                    valid_forms.append(form)
                else:
                    any_errors = True

        if not any_errors:
            for form in valid_forms:
                form.save()
            return redirect('login')  # Redirige a la página principal después de guardar
    else:
        formset = [ProductoForm(prefix=str(i)) for i in range(3)]
    return render(request, 'ingresarproductos.html', {'formset': formset})
    """


def activar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.estado = 'Activado'
    producto.save()
    return redirect('ver_catalogo_admin', catalogo_id=producto.catalogo.id)


def desactivar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.estado = 'Desactivado'
    producto.save()
    return redirect('ver_catalogo_admin', catalogo_id=producto.catalogo.id)


def actualizarproducto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoActualizarForm(request.POST, request.FILES, instance=producto)  # Vincula el formulario con el platillo existente
        if form.is_valid():
            form.save()
            return redirect('ver_catalogo_admin', catalogo_id=producto.catalogo.id)  # Redirigir a una URL después de actualizar el formulario
    else:
        form = ProductoActualizarForm(instance=producto)
    data = {'form': form, 'titulo': 'Actualizar producto'}
    return render(request, 'ingresarproductos.html', data)
