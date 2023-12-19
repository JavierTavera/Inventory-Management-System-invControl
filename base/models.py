from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bodega(models.Model):
    nombre = models.CharField(max_length=80)
    desc = models.CharField(max_length=200, null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=80)
    desc = models.CharField(max_length=200, null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class EstadoProducto(models.Model):
    estado = models.CharField(max_length=80)

    def __str__(self):
        return self.estado

class TipoProducto(models.Model):
    tipo = models.CharField(max_length=80)

    def __str__(self):
        return self.tipo

class Referencia(models.Model):
    IdReferencia = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=80, null=True, blank=True)
    descripcion = models.CharField(max_length=80, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.IdReferencia
