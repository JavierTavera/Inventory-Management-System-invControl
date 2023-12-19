from django.forms import ModelForm, TextInput, Select
from .models import Referencia

class ReferenciaForm(ModelForm):

    class Meta:
        model = Referencia
        fields = '__all__'
        labels = {
            'usuario': '',
            'IdReferencia': 'Código Referencia',
            'tipo': 'Tipo de Producto',
            'nombre': 'Nombre del Producto (Opcional)',
            'descripcion': 'Descripción (Opcional)'
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
