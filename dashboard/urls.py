from django.urls import include, path
from .views import GeneratePdf

from .views import *

urlpatterns = [
    path('dashboard', dashboard, name='dashboard'),
    # Usuarios
    path('dashboard/usuarios', usuarios, name='dashboard-usuarios'),
    path('dashboard/usuarios/agregar', agregar_usuario, name='dashboard-agregar-usuario'),
    path('dashboard/usuarios/editar/<id>', editar_usuario, name='editar-usuario'),
    path('dashboard/usuarios/eliminar/<id>', eliminar_usuario, name='eliminar-usuario'),
    # Productos
    path('dashboard/productos', productos, name='dashboard-productos'),
    path('dashboard/productos/agregar', agregar_producto, name='dashboard-agregar-producto'),
    path('dashboard/productos/editar/<id>', editar_producto, name='editar-producto'),
    path('dashboard/productos/eliminar/<id>', eliminar_producto, name='eliminar-producto'),
    # Vehículos
    path('dashboard/vehiculos', vehiculos, name='dashboard-vehiculos'),
    path('dashboard/vehiculos/agregar', agregar_vehiculo, name='dashboard-agregar-vehiculo'),
    path('dashboard/vehiculos/editar/<id>', editar_vehiculo, name='editar-vehiculo'),
    path('dashboard/vehiculos/eliminar/<id>', eliminar_vehiculo, name='eliminar-vehiculo'),

    path('dashboard/templates/index', index, name='index'),
    path('pdf/', GeneratePdf.as_view(),name='pdf'),
]