from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bodega, Proveedor, Referencia, Producto
from .forms import ReferenciaForm, ProductoForm

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

# los_proveedores = [
#     {'id': 1, 'nombre': 'Europa'},
#     {'id': 2, 'nombre': 'USA'}
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
    las_bodegas = Bodega.objects.all().order_by('id')
    context = {'las_bodegas': las_bodegas}
    return render(request, 'base/bodegas.html', context)

def proveedores(request):
    los_proveedores = Proveedor.objects.all().order_by('id')
    context = {'los_proveedores': los_proveedores}
    return render(request, 'base/proveedores.html', context)

def ingreso_productos(request, pk):
    las_referencias = Referencia.objects.all().filter(tipo=pk)
    ref_bool = False
    #print(las_referencias)
    if int(pk)<=5 and int(pk)>=1:
        ref_bool = True
        #print(las_referencias[0])
    if ref_bool:
        context = {'las_referencias': las_referencias, 'el_tipo_producto': las_referencias[0]}
        return render(request, 'base/ingreso_productos.html', context)
    else:
        return render(request, 'base/productos.html')

def ingreso_manual(request, pk):
    current_user = request.user if request.user.is_authenticated else None
    form = ProductoForm(initial={'usuario': current_user, 'IdReferencia': pk})
    if request.method == 'POST':
        # print(request.POST)
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingreso_manual')
    context = {'form': form}
    return render(request, 'base/ingreso_productos/ingreso_manual.html', context)

def ingreso_referencias(request):
    current_user = request.user if request.user.is_authenticated else None
    form = ReferenciaForm(initial={'usuario': current_user})
    if request.method == 'POST':
        # print(request.POST)
        form = ReferenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingreso_referencias')
    context = {'form': form}
    return render(request, 'base/ingreso_referencias.html', context)

# De aquí para abajo son ejemplos


def transferencias_stock(request):
    return render(request, 'base/DeEjemplo/transferencias_stock.html')

def ajuste_de_inventario(request):
    return render(request, 'base/DeEjemplo/ajuste_de_inventario.html')

def ordenes_de_ventas(request):
    return render(request, 'base/DeEjemplo/ordenes_de_ventas.html')
