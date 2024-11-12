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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from PaginaWeb.views import portalpago,ingresarproducto
from PaginaWeb.views import verproducto
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

from Pedido_app.views import consultar_pedidos,ver_pedido

from Carrito_app.views import ver_carrito, agregar_a_carrito, aumentar_cantidad
from Carrito_app.views import disminuir_cantidad,realizar_pedido,pagoexitoso
from Carrito_app.views import pagofracaso

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
    
    path('ver_producto/',verproducto),
    path('ingresar_producto/',ingresarproducto, name='ingresar_producto'),
    path('activar_producto/<int:producto_id>/',activar_producto, name='activar_producto'),
    path('desactivar_producto/<int:producto_id>/',desactivar_producto, name='desactivar_producto'),
    path('actualizar_producto/<int:producto_id>/',actualizarproducto, name='actualizar_producto'),
    
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

    path('pedidos/',consultar_pedidos),
    path('ver_pedido/<int:pedido_id>/',ver_pedido),

    path('mi_carrito/<int:usuario_id>',ver_carrito,name="mi_carrito"),
    path('agregar_a_carrito/<int:producto_id>',agregar_a_carrito,name="agregar_a_carrito"),
    path('aumentar_cantidad/<int:pedido_carrito_id>',aumentar_cantidad,name='aumentar_cantidad'),
    path('disminuir_cantidad/<int:pedido_carrito_id>',disminuir_cantidad,name='disminuir_cantidad'),
    path('realizar_pedido/',realizar_pedido,name='realizar_pedido'),
    path('pago fracaso/',pagofracaso),
    path('pago exitoso/',pagoexitoso),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
