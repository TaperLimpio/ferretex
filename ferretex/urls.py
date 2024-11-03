"""
URL configuration for ferretex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from PaginaWeb.views import portalpago,ingresarproducto,carritocompra
from PaginaWeb.views import verproducto,pagofracaso,pagoexitoso
from PaginaWeb.views import ingresarcatalogo, paginaprincipal,ingresarlocal
from PaginaWeb.views import Administrador,Repartidor

from Usuario_app.views import Login, CrearCuenta, CrearCuentaAdmin
from Usuario_app.views import ver_usuario, Update_Usuario, delete_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login, name='login'),
    path('usuarios/<int:emp_id>/',ver_usuario, name='ver_usuario'),
    path('crear-cuenta/', CrearCuenta,name='crear_cuenta'),
    path('pagina-admin/', Administrador,name='administrador'),
    path('crear-cuenta-admin/', CrearCuentaAdmin,name='crear_cuenta_admin'),
    path('pagina-repartidor/', Repartidor,name='repartidor'),
    path('delete-usuario/<int:emp_id>/',delete_usuario, name='delete_usuario'),
    path('portal_pago/',portalpago),
    path('ingresar_platillo/',ingresarproducto),
    path('carrito_de_compra/',carritocompra),
    path('pago fracaso/',pagofracaso),
    path('pago exitoso/',pagoexitoso),
    path('ingresar catalogo/',ingresarcatalogo),
    path('ingresar sucursal/',ingresarlocal),
    path('ver_producto/',verproducto),
    path('update_usuario/<int:emp_id>/', Update_Usuario),
    path('pagina_principal/',paginaprincipal,name='usuario')
]
