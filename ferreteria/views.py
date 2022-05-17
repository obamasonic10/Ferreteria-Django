from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Producto
from .models import Solicitud

from .forms import ProductoForm
from .forms import SolicitudForm

# Create your views here.

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

#PRODUCTOS
#@login_required
def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {'productos': productos})

def agregar(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/agregar.html', {'formulario': formulario})

def editar(request, id):
    producto = Producto.objects.get(id=id)
    formulario = ProductoForm(request.POST or None, request.FILES or None, instance=producto)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/editar.html', {'formulario': formulario})

def eliminar(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('productos')


#LOGIN
def login(request):
    return render(request, 'paginas/login.html')


#MAESTROS
def solicitudes(request):
    solicitudes = Solicitud.objects.all()
    return render(request, 'maestros/indexMaestro.html', {'solicitudes': solicitudes})

def rechazar(request, id):
    solicitud = Solicitud.objects.get(id=id)
    solicitud.delete()
    return redirect('solicitudes')

#CLIENTES
def inicioCliente(request):
    return render(request, 'cliente/inicioCliente.html')

def crearSolicitud(request):
    form = SolicitudForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('crearSolicitud')
    return render(request, 'cliente/crearSolicitud.html', {'form': form})
