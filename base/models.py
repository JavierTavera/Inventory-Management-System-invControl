from django.db import models
from django.contrib.auth.models import User
import uuid

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
    IdProveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)
    tipo = models.ForeignKey(TipoProducto, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=80, null=True, blank=True)
    descripcion = models.CharField(max_length=80, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.IdReferencia

class Producto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    IdReferencia = models.ForeignKey(Referencia, on_delete=models.SET_NULL, null=True)
    IdEstado_producto = models.ForeignKey(EstadoProducto, on_delete=models.SET_NULL, null=True)
    IdBodega = models.ForeignKey(Bodega, on_delete=models.SET_NULL, null=True)
    codigoQR = models.CharField(max_length=200, null=True, blank=True)
    lote = models.CharField(max_length=30)

    fecha_vencimiento = models.CharField(max_length=30, null=True, blank=True)

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

class Transacciones(models.Model):
    IdProducto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    IdEstado_producto = models.ForeignKey(EstadoProducto, on_delete=models.SET_NULL, null=True)
    otro_estado = models.CharField(max_length=80, null=True, blank=True)
    IdBodega = models.ForeignKey(Bodega, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.IdProducto
