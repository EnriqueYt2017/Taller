from django.urls import path, include
from .views import *
from rest_framework import routers

# CONFIGURACION PARA API
router = routers.DefaultRouter()
router.register('Vehiculos', VehiculoViewset)



urlpatterns = [
    path('', home, name="home"),
    path('contactos', contactos, name="contactos"),
    path('listado_autos', listado_autos, name="listado_autos"),
    path('informacion_auto', informacion_auto, name="informacion_auto"),
    path('login', login_view, name="login"),
    path('register', register, name="register"),
    path('about', about, name="about"),
    path('agendar_hora', agendar_hora, name="agendar_hora"),
    path('formulario', formulario, name="formulario"),
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
    path('vehiculos/update/<nombre>', vehiculosupdate, name="vehiculosupdate"),
    path('vehiculos/delete/<nombre>', vehiculosdelete, name="vehiculosdelete"),
]
