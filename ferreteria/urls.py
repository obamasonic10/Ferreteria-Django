from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.productos, name='productos'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('productos', views.productos, name='productos'),
    path('agregar', views.agregar, name='agregar'),
    path('productos/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('productos/editar/<int:id>', views.editar, name='editar'),

    path('login', views.login, name='login'),

    path('indexMaestro', views.solicitudes, name='solicitudes'),
    path('rechazar/<int:id>', views.rechazar, name='rechazar'),

    path('inicioCliente', views.inicioCliente, name='inicioCliente'),
    path('crearSolicitud', views.crearSolicitud, name='crearSolicitud'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)