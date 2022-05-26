from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

from ferreteria.views import tienda, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito

urlpatterns = [
    path('', views.productos, name='productos'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('productos', views.productos, name='productos'),
    path('agregar', views.agregar, name='agregar'),
    path('productos/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('productos/editar/<int:id>', views.editar, name='editar'),

    path('login/', views.login, name='login'),
    path('registroEmpresas/', views.registroEmpresas, name='registroEmpresas'),

    path('indexMaestro', views.solicitudes, name='solicitudes'),
    path('rechazar/<int:id>', views.rechazar, name='rechazar'),

    path('inicioCliente', views.inicioCliente, name='inicioCliente'),
    path('crearSolicitud', views.crearSolicitud, name='crearSolicitud'),

    path('tienda', views.tienda, name='tienda'),
    path('agregar/<int:producto_id>', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)