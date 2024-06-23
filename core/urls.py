from django.urls import path, include
from .views import *
from rest_framework import routers

# CONFIGURACIÓN PARA API
router = routers.DefaultRouter()
router.register('Vehiculos', VehiculoViewset)



urlpatterns = [
    path('', home, name="home"),
    path('contactos', contactos, name="contactos"),
    path('listado_autos', listado_autos, name="listado_autos"),
    path('informacion_auto', informacion_auto, name="informacion_auto"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout2"),
    path('register', register, name="register"),
    path('about', about, name="about"),
    path('agendar_hora', agendar_hora, name="agendar_hora"),
    path('formulario', formulario, name="formulario"),
    path('pagos', pagos, name="pagos"),
    # USUARIOS
    path('empleados', empleados, name="empleados"),
    path('empleados/add/', empleadosadd, name="empleadosadd"),
    path('empleados/update/<nombre>', empleadosupdate, name="empleadosupdate"),
    path('empleados/delete/<nombre>', empleadosdelete, name="empleadosdelete"),
    # API
    #path('api/' , include(router.urls)),
    #path('usuariosapi', usuariosapi, name="usuariosapi"),

    # VEHICULOS
    path('vehiculos', vehiculos, name="vehiculos"),
    path('vehiculos/add/', vehiculosadd, name="vehiculosadd"),
    path('vehiculos/update/<propietario>', vehiculosupdate, name="vehiculosupdate"),
    path('vehiculos/delete/<propietario>', vehiculosdelete, name="vehiculosdelete"),
    path('vehiculos/view', vehiculosview, name="vehiculosview"),
]
