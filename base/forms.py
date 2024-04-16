from django.forms import ModelForm, TextInput, Select
from .models import Referencia, Producto, Bodega

class ReferenciaForm(ModelForm):

    class Meta:
        model = Referencia
        fields = '__all__'
        labels = {
            'id': 'ID',
            'usuario': '',
            'IdReferencia': 'Código Referencia',
            'tipo': 'Tipo de Producto',
            'nombre': 'Nombre del Producto (Opcional)',
            'descripcion': 'Descripción (Opcional)',
            'IdProveedor': 'Proveedor'
        }
        widgets = {
            'id': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Código de referencia'
            }),
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


class ProductoForm2(ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
        labels = {
            'IdReferencia': 'Referencia',
            'IdEstado_producto': 'Estado producto',
            'IdBodega': 'Bodega',
            'codigoQR': 'codigo QR (Opcional)',
            'lote': 'Lote',
            'fecha_vencimiento': '',
            'usuario': ''
        }
        widgets = {
            'IdReferencia': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
            }),
            'IdEstado_producto': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
            }),
            'IdBodega': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
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
                'placeholder': 'Ej: 20-12-2026',
                'hidden': ''
            }),
            'usuario': Select(attrs={
                'hidden': ''
            })
        }


class ProductoForm2_disabled(ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
        labels = {
            'IdReferencia': 'Referencia',
            'IdEstado_producto': 'Producto',
            'IdBodega': 'Bodega',
            'codigoQR': 'codigo QR (Opcional)',
            'lote': 'Lote',
            'fecha_vencimiento': '',
            'usuario': ''
        }
        widgets = {
            'IdReferencia': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'disabled': 'True'
            }),
            'IdEstado_producto': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'disabled': 'True'
            }),
            'IdBodega': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'disabled': 'True'
            }),
            'codigoQR': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'codigo QR',
                'disabled': 'True'
            }),
            'lote': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Lote',
                'disabled': 'True'
            }),
            'fecha_vencimiento': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Ej: 20-12-2026',
                'disabled': 'True',
                'hidden': ''
            }),
            'usuario': Select(attrs={
                'hidden': ''
            })
        }
    

class BodegaForm(ModelForm):

    class Meta:
        model = Bodega
        fields = ['nombre']
        labels = {
            'nombre': 'Bodega'
        }
        widgets = {
            'nombre': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
            })
        }



class TransferenciaForm(ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'
        labels = {
            'IdReferencia': '',
            'IdEstado_producto': '',
            'IdBodega': '',
            'codigoQR': 'codigo QR',
            'lote': 'Lote',
            'fecha_vencimiento': '',
            'usuario': ''
        }
        widgets = {
            'IdReferencia': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'hidden': ''
            }),
            'IdEstado_producto': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'hidden': ''
            }),
            'IdBodega': Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
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
                'placeholder': 'Ej: 20-12-2026',
                'hidden': ''
            }),
            'usuario': Select(attrs={
                'hidden': ''
            })
        }