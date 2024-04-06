from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboards/<str:pk>/', views.dashboards, name="dashboards"),
    path('dashboard_producto/<str:pk>/', views.dashboard_producto, name="dashboard_producto"),
    path('bodega_producto/', views.bodega_producto, name="bodega_producto"),
    path('items/<str:pk>/', views.items_pk, name="items_pk"),
    path('items/', views.items, name="items"),
    path('bodegas/', views.bodegas),
    path('proveedores/', views.proveedores),
    path('ingreso_productos/<str:pk>/', views.ingreso_productos, name="ingreso_productos"),
    path('ingreso_productos/ingreso_manual/<str:pk>/', views.ingreso_manual, name="ingreso_manual"),
    path('ingreso_productos/ingreso_qr/<str:pk>/', views.ingreso_qr, name="ingreso_qr"),
    path('ingreso_referencias/', views.ingreso_referencias, name="ingreso_referencias"),

    path('transferencias_stock/', views.transferencias_stock),
    path('recepcion_stock/', views.transferencias_stock, name="transferencias_stock"),
    path('ajuste_de_inventario/', views.ajuste_de_inventario),
    path('ordenes_de_ventas/', views.ordenes_de_ventas),
]