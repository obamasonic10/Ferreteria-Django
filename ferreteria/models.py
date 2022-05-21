import datetime
from email import charset
from django.db import models

# Create your models here.
# De hacer cambios, volver a hacer python manage.py makemigrations y aceptar (y) -> 
#                               -> python manage.py migrate
class Admin(models.Model):
    rutAdmin = models.CharField('Rut Administrador', max_length=12, primary_key=True)
    nombreAdmin= models.CharField('Nombre Administrador', max_length=60)
    apellidopAdmin= models.CharField('Apellido Paterno Administrador', max_length=60)
    apellidomAdmin= models.CharField('Apellido Materno Administrador', max_length=60)
    password = models.CharField('Password', max_length=60)

    def __str__(self):
        return self.nombreAdmin


class Comuna(models.Model):
    idcomuna=models.AutoField('id Comuna', primary_key=True)
    nombreComuna = models.CharField('Nombre Comuna', max_length=50)

    def __str__(self):
        return self.nombreComuna


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='imagen', null=True)
    nombre = models.CharField(max_length=60, verbose_name='nombre')
    marca = models.CharField(max_length=15, verbose_name='marca')
    categoria = models.CharField(max_length=15, null=True,verbose_name='categoria')
    descripcion = models.TextField(max_length=100, verbose_name='descripción')            
    stock = models.IntegerField(verbose_name='stock')
    fechavenc = models.DateField(verbose_name='fecha vencimiento', auto_now=False, auto_now_add=False, blank=True, null=True)                   
    precioventa = models.IntegerField(verbose_name='precio venta')  

    def __str__(self):
        fila = "nombre: " + self.nombre + " - " + "marca: " + self.marca + " - " + "categoria: " + self.categoria + "-" + "descripcion: " + self.descripcion + " - " + "stock: " + str(self.stock) + " - " +  "fecha vencimiento" + str(self.fechavenc) + " - " + "precio venta: $" + str(self.precioventa)
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()         


class Solicitud(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30, verbose_name='título')
    tipotrabajo = models.CharField(max_length=30, verbose_name='tipo de trabajo', null=True)
    descripcion = models.TextField(max_length=100, verbose_name='descripción del trabajo')
    imagensol = models.ImageField(upload_to='imagenes/', verbose_name='imagen')
    nombre = models.CharField(max_length=60, verbose_name='nombre solicitante')
    celular = models.CharField(max_length=12,verbose_name='celular')
    correo = models.EmailField(max_length=30, verbose_name='correo')

    def __str__(self):
        fila = "título: " + self.titulo + " - " + "tipo de trabajo: " + self.tipotrabajo + " - " + "descripción del trabajo: " + self.descripcion + " - " + "nombre solicitante: " + self.nombre + " - " + "celular: " + self.celular + " - " + "correo: " + self.correo
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagensol.storage.delete(self.imagensol.name)
        super().delete()  