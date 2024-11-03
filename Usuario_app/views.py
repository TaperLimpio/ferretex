from django.shortcuts import render, redirect, get_object_or_404
from Usuario_app.models import Usuario
from . import forms
from .forms import UsuarioForm, UsuarioAdminForm

def Login(request):
    if request.method == 'POST':
        nombre = request.POST.get('username')
        contraseña = request.POST.get('contraseña')  # Agregamos el campo fono
        usuario = Usuario.objects.filter(nombre=nombre, contraseña=contraseña).first()  # Usamos filter() y first()
        if usuario and usuario.estado == 'activo':
            request.session['usuario_id'] = usuario.id
            if usuario.tipo == 'usuario':
                return redirect('usuario')  # Redirigir a la URL 'usuario'
            elif usuario.tipo == 'administrador':
                return redirect('administrador')  # Redirigir a la URL 'administrador'
            elif usuario.tipo=='repartidor':
                return redirect('repartidor')#lo mismo pero para el repartidor
        else:
            return render(request, 'login.html', {'error': 'Usuario inválido'})
    return render(request, 'login.html')

def CrearCuenta(request):
    form = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.estado='activo'
            usuario.tipo = 'usuario'  # Establecer el tipo a 'usuario' automáticamente
            usuario.save()
            return redirect('login')  # Redirigir al login después de crear la cuenta
    data = {'form': form, 'titulo': 'Crear cuenta'}
    return render(request, 'crear-cuenta.html', data)

def CrearCuentaAdmin(request):
    if request.method == 'POST':
        form = UsuarioAdminForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.estado='activo'
            form.save()
            return redirect('login')  # Redirigir al login después de crear la cuenta
    else:
        form = UsuarioAdminForm()
    data = {'form': form, 'titulo': 'Crear cuenta de administrador'}
    return render(request, 'crear-cuenta-admin.html', data)

def ver_usuario(request, emp_id):
    usuario = get_object_or_404(Usuario, id=emp_id)
    return render(request, 'view-usuario.html', {'usuario': usuario})

def Update_Usuario(request, emp_id):
    usuario = Usuario.objects.get(id=emp_id)
    form = UsuarioForm(instance=usuario)
    
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir al login después de actualizar
        
    data = {'form': form, 'titulo': 'Actualizar usuario'}
    return render(request, 'crear-cuenta.html', data)

def delete_usuario(request, emp_id):
    usuario = Usuario.objects.get(id=emp_id)
    if usuario:
        usuario.estado = 'inactivo'
        usuario.save()
    return redirect('login')