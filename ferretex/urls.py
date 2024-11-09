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
from PaginaWeb.views import paginaprincipal
from PaginaWeb.views import Repartidor

from Usuario_app.views import Login, CrearCuenta, CrearCuentaAdmin
from Usuario_app.views import ver_usuario, Update_Usuario, delete_usuario
from Usuario_app.views import Index_Usuario

from Producto_app.views import ingresarproducto,activar_producto,desactivar_producto
from Producto_app.views import actualizarproducto

from Catalogo_app.views import ingresarcatalogo,paginaprincipal,paginaadmin
from Catalogo_app.views import actualizarcatalogo,asignar_producto,ver_catalogo
from Catalogo_app.views import ver_catalogoadmin,activar_catalogo,desactivar_catalogo

from Sucursal_app.views import listasucursal, ingresarsucursal, consultarsucursal
from Sucursal_app.views import modificarsucursal, deshabilitarsucursal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login, name='login'),
    path('usuarios/<int:emp_id>/',ver_usuario, name='ver_usuario'),
    path('crear-cuenta/', CrearCuenta,name='crear_cuenta'),
    path('crear-cuenta-admin/', CrearCuentaAdmin,name='crear_cuenta_admin'),
    path('index usuario/', Index_Usuario, name='index_usuario'),
    path('pagina-repartidor/', Repartidor,name='repartidor'),
    path('delete-usuario/<int:emp_id>/',delete_usuario, name='delete_usuario'),
    path('update_usuario/<int:emp_id>/', Update_Usuario),
    path('pagina_principal/',paginaprincipal,name='pagina_principal'),
    path('pagina-admin/', paginaadmin, name='pagina_administrador'),
    path('portal_pago/',portalpago),

    path('carrito_de_compra/',carritocompra),
    path('pago fracaso/',pagofracaso),
    path('pago exitoso/',pagoexitoso),
    
    path('ver_producto/',verproducto),
    path('ingresar_producto/',ingresarproducto, name='ingresar_platillo'),
    path('activar_producto/<int:platillo_id>/',activar_producto, name='activar_platillo'),
    path('desactivar_producto/<int:platillo_id>/',desactivar_producto, name='desactivar_platillo'),
    path('actualizar_platillo/<int:platillo_id>/',actualizarproducto, name='actualizar_platillo'),
    
    path('ingresar_catalogo/',ingresarcatalogo,name='ingresar_catalogo'),
    path('ver_catalogo/<int:catalogo_id>/', ver_catalogo, name='ver_catalogo'), 
    path('actualizar_catalogo/<int:catalogo_id>/', actualizarcatalogo, name='actualizar_catalogo'),
    path('asignar_platillo/<int:catalogo_id>/', asignar_producto, name='asignar_platillo'),
    path('pagina-admin/', paginaadmin, name='pagina_administrador'),
    path('ver_catalogo_admin/<int:catalogo_id>/', ver_catalogoadmin, name='ver_catalogo_admin'),
    path('activar_catalogo/<int:catalogo_id>/',activar_catalogo, name='activar_catalogo'),
    path('desactivar_catalogo/<int:catalogo_id>/',desactivar_catalogo, name='desactivar_catalogo'),

    path('lista_sucursales/', listasucursal),
    path('ingresar sucursal/',ingresarsucursal),
    path('consultar_sucursal/<int:id>/', consultarsucursal),
    path('modificar_sucursal/<int:id>/', modificarsucursal),
    path('deshabilitar_sucursal/<int:id>/', deshabilitarsucursal),

]