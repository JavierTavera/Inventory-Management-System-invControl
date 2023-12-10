from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('items/<str:pk>/', views.items_pk, name="items_pk"),
    path('items/', views.items, name="items"),

    path('transferencias_stock/', views.transferencias_stock),
    path('bodegas/', views.bodegas),
    path('ajuste_de_inventario/', views.ajuste_de_inventario),
    path('ordenes_de_ventas/', views.ordenes_de_ventas),
    path('ordenes_de_compra/', views.ordenes_de_compra),
]