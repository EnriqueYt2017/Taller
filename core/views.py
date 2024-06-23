from django.shortcuts import redirect, render
from .models import *
from .form import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework import viewsets
from .serializers import *
from rest_framework.renderers import JSONRenderer
import requests
from django.http import JsonResponse
from django.views import View

#API
def usuariosapi(request):
    response = requests.get('https://rickandmortyapi.com/api/character')
    response2 = requests.get('https://digimon-api.vercel.app/api/digimon')
    usuarios = response.json()
    digimons = response2.json()

    aux = {
        'lista' : usuarios,
        'listadigimons' : digimons
    }
    return render(request, 'core/crudapi/index.html', aux)

#UTILIZAMOS LOS VIEWSET PARA MANEJAR LAS SOLICITUDES HTTP (GET,POST,PUT,DELETE)
class VehiculoViewset(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


# Create your views here.
def home(request):
    vehiculos = Vehiculo.objects.all()
    aux = {
        'lista' : vehiculos
    }
    return render(request, 'core/home.html', aux)

@login_required
def contactos(request):
    aux = {
        'breadcrumb' : {
            'title' : 'Contáctenos',
            'links' : ['Contáctenos']
        }
    }
    return render(request, 'core/contactos.html', aux)

def listado_autos(request):
    return render(request, 'core/listado_autos.html')

def informacion_auto(request):
    return render(request, 'core/informacion_auto.html')

def login_view(request):
    return render(request, 'registration/login.html')

#SOLO LA VERA EL ADMIN
def about(request):
    aux = {
        'breadcrumb' : {
            'title' : 'Acerca de Nosotros',
            'links' : ['Acerca de Nosotros']
        }
    }
    return render(request, 'core/about.html', aux)

def agendar_hora(request):
    return render(request, 'core/agendar_hora.html')

def register(request):
    aux = {
        'form' : CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            #ASIGNAMOS UN GRUPO AL USUARIO CREADO
            grupo = Group.objects.get(name='Usuarios')
            user.groups.add(grupo)
            # MENSAJE
            messages.success(request, 'Usuario Registrado')    
            # AUTENTICA Y LOGEA
            user = authenticate(username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login( request, user)
            # LO MANDA A UNA PAGINA
            return redirect(to="home")
        else:
            aux['form'] = formulario
    return render(request, 'registration/register.html', aux)


def empleados (request):
    empleados = Empleado.objects.all()
    aux = {
        'lista' : empleados
    }
    
    return render(request, 'core/empleados/index.html', aux)

def empleadosadd(request):
    empleados = Empleado.objects.all()
    aux = {
        'form' : EmpleadoForm()
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Empleado Agregado')
        else:
            aux['form'] = formulario
            messages.error(request, 'Error al Agregar')

    return render(request, 'core/empleados/crud/add.html', aux)

def empleadosupdate(request, nombre):
    empleados = Empleado.objects.get(nombre=nombre)
    aux = {
        'form' : EmpleadoForm(instance=empleados)
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(data=request.POST, instance=empleados, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Empleado Modificado')
        else:
            aux['form'] = formulario
            messages.error(request, 'Error al Modificar')

    return render(request, 'core/empleados/crud/update.html',aux)

def empleadosdelete(request, nombre):
    empleados = Empleado.objects.get(nombre=nombre)
    empleados.delete()
    return redirect(to="empleados")

def formulario(request):
    return render(request, 'core/formulario.html')


#VEHÍCULOS ADD UPDATE DELETE
def vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    aux = {
        'lista' : vehiculos,
        'breadcrumb' : {
            'title' : 'Listado de autos',
            'links' : ['Listado']
        }
    }
    return render(request, 'core/vehiculos/index.html', aux)

def vehiculosadd(request):
    vehiculos = Vehiculo.objects.all()
    aux = {
        'form' : VehiculoForm(),
        'breadcrumb' : {
            'title' : 'Añadir Vehículo',
            'links' : ['Información Auto', 'Añadir Vehículo']
        }
    }

    if request.method == 'POST':
        formulario = VehiculoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Vehiculo Agregado')
        else:
            aux['form'] = formulario
            messages.error(request, 'Error al Agregar')

    return render(request, 'core/vehiculos/crud/add.html', aux)

def vehiculosupdate(request, propietario):
    vehiculos = Vehiculo.objects.get(propietario=propietario)
    aux = {
        'form' : VehiculoForm(instance=vehiculos)
    }

    if request.method == 'POST':
        formulario = VehiculoForm(data=request.POST, instance=vehiculos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Vehiculo Modificado')
        else:
            aux['form'] = formulario
            messages.error(request, 'Error al Modificar')
    return render(request, 'core/vehiculos/crud/update.html', aux)

def vehiculosdelete(request, propietario):
    vehiculos = Vehiculo.objects.get(propietario=propietario)
    vehiculos.delete()
    return redirect(to="vehiculos")

def vehiculosview():
    return render(request, 'core/vehiculos/crud/view.html', aux)

def pagos():
    return render(request, 'core/pagos.html', aux)

def logout_view(request):
    logout(request)
    return redirect(to="home")

class SearchVehiclesView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        vehicles = Vehicle.objects.filter(name__istartswith=query)
        results = list(vehicles.values('name', 'other_field'))
        return JsonResponse(results, safe=False)