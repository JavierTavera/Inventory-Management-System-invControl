from django.forms import ModelForm, TextInput, Select
from .models import Referencia, Producto

class ReferenciaForm(ModelForm):

    class Meta:
        model = Referencia
        fields = '__all__'
        labels = {
            'usuario': '',
            'IdReferencia': 'Código Referencia',
            'tipo': 'Tipo de Producto',
            'nombre': 'Nombre del Producto (Opcional)',
            'descripcion': 'Descripción (Opcional)',
            'IdProveedor': 'Proveedor'
        }
        widgets = {
            'IdReferencia': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Código de referencia'
            }),
            'tipo': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
            }),
            'IdProveedor': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
            }),
            'nombre': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Nombre Producto'
            }),
            'descripcion': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Descripción'
            }),
            'usuario': Select(attrs={
                'hidden': ''
            })
        }


class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
        labels = {
            'IdReferencia': '',
            'IdEstado_producto': '',
            'IdBodega': '',
            'codigoQR': 'codigo QR (Opcional)',
            'lote': 'Lote',
            'fecha_vencimiento': 'Fecha vencimiento (DD-MM-AAAA) (Opcional)',
            'usuario': ''
        }
        widgets = {
            'IdReferencia': TextInput(attrs={
                'hidden': ''
            }),
            'IdEstado_producto': Select(attrs={
                'hidden': ''
            }),
            'IdBodega': Select(attrs={
                'hidden': ''
            }),
            'codigoQR': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'codigo QR'
            }),
            'lote': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Lote'
            }),
            'fecha_vencimiento': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Ej: 20-12-2026'
            }),
            'usuario': Select(attrs={
                'hidden': ''
            })
        }
