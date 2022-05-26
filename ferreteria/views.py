from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

from ferreteria.Carrito import Carrito

import mysql.connector as sql

rut=''
nombre=''
apellidoP=''
apellidoM=''
email=''
celular=''
password=''
comuna=''

# Create your views here.
#LOGIN
def login(request):
    return render(request, 'paginas/login.html')


def nosotros(request):
    return render(request, 'paginas/nosotros.html')

#REGISTRO EMPRESAS
#QUERY para registrar
def registroEmpresas(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='ferretec')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="rutAdmin":
                rut=value
            if key=="nombreAdmin":
                nombre=value
            if key=="apellidopAdmin":
                apellidoP=value
            if key=="apellidomAdmin":
                apellidoM=value
            if key=="password":
                password=value


        c="INSERT INTO `ferreteria_cliente` Values('{}','{}','{}','{}',MD5('{}'))".format(rut,nombre,apellidoP,apellidoM,email,celular,password,comuna)
        cursor.execute(c)
        m.commit()

    return render(request,'paginas/registroEmpresas.html')


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


#TIENDA
def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos': productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("tienda")