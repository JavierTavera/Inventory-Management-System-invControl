from django.contrib import admin

# Register your models here.

from .models import Bodega, Proveedor, EstadoProducto, TipoProducto, Referencia, Producto, Transacciones

class ProductoFilter(admin.ModelAdmin):
    list_display = ["usuario", "IdEstado_producto", "IdBodega", "codigoQR", "lote", "fecha_vencimiento", "creado", "actualizado"]
    list_filter = ["usuario", "IdEstado_producto", "IdBodega", "codigoQR", "lote", "fecha_vencimiento", "creado", "actualizado"]

admin.site.register(Bodega)
admin.site.register(Proveedor)
admin.site.register(EstadoProducto)
admin.site.register(TipoProducto)
admin.site.register(Referencia)
admin.site.register(Producto, ProductoFilter)
admin.site.register(Transacciones)

