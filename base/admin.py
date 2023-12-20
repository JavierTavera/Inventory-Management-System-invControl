from django.contrib import admin

# Register your models here.

from .models import Bodega, Proveedor, EstadoProducto, TipoProducto, Referencia, Producto, Transacciones

admin.site.register(Bodega)
admin.site.register(Proveedor)
admin.site.register(EstadoProducto)
admin.site.register(TipoProducto)
admin.site.register(Referencia)
admin.site.register(Producto)
admin.site.register(Transacciones)

