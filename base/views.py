from django.shortcuts import render
from django.http import HttpResponse
from .models import Bodega

items_p = [
    {'id': 1, 'name': 'Prótesis 1', 'lote': 'LOTE1', 'type': 'Prótesis', 'stock': 5, 'fecha_rec': '20-11-2023'},
    {'id': 2, 'name': 'Prótesis 2', 'lote': 'LOTE2', 'type': 'Prótesis', 'stock': 11, 'fecha_rec': '19-11-2023'},
    {'id': 3, 'name': 'Prótesis 3', 'lote': 'LOTE3', 'type': 'Prótesis', 'stock': 7, 'fecha_rec': '21-11-2023'},
    {'id': 4, 'name': 'Cinta 1', 'lote': 'LOTE4', 'type': 'Cinta', 'stock': 20, 'fecha_rec': '01-11-2023'},
    {'id': 5, 'name': 'Cinta 2', 'lote': 'LOTE5', 'type': 'Cinta', 'stock': 15, 'fecha_rec': '03-11-2023'}
]

products = [
    {'id': 1, 'type': 'Prótesis', 'SKU': 'SKU1', 'lote': 'LOTE1'},
    {'id': 2, 'type': 'Prótesis', 'SKU': 'SKU2', 'lote': 'LOTE1'},
    {'id': 3, 'type': 'Prótesis', 'SKU': 'SKU3', 'lote': 'LOTE2'},
    {'id': 4, 'type': 'Cinta', 'SKU': 'SKU4', 'lote': 'LOTE4'}
]

# las_bodegas = [
#     {'id': 1, 'nombre': 'Bogotá'},
#     {'id': 2, 'nombre': 'Medellín'}
# ]
def home(request):
    return render(request, 'base/login.html')

def dashboard(request):
    context = {'products': products}
    return render(request, 'base/dashboard.html', context)

def items_pk(request, pk):
    it_bool = False
    items_id = None
    for ite in items_p:
        if ite['id'] == int(pk):
            it_bool = True
            items_id = ite
    if it_bool:
        context = {'items_id': items_id}
        return render(request, 'base/items_det.html', context)
    else:
        context = {'items_p': items_p}
        return render(request, 'base/items.html', context)

def items(request):
    context = {'items_p': items_p}
    return render(request, 'base/items.html', context)

def bodegas(request):
    las_bodegas = Bodega.objects.all()
    context = {'las_bodegas': las_bodegas}
    return render(request, 'base/bodegas.html', context)


# De aquí para abajo son ejemplo


def transferencias_stock(request):
    return render(request, 'base/DeEjemplo/transferencias_stock.html')

def ajuste_de_inventario(request):
    return render(request, 'base/DeEjemplo/ajuste_de_inventario.html')

def ordenes_de_ventas(request):
    return render(request, 'base/DeEjemplo/ordenes_de_ventas.html')

def ordenes_de_compra(request):
    return render(request, 'base/DeEjemplo/ordenes_de_compra.html')