import csv
import json
from datetime import datetime

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import get_template, render_to_string
from django.views import View
from django.views.generic import ListView
from rest_framework import filters, viewsets
from rest_framework.renderers import JSONRenderer
from xhtml2pdf import pisa

from core.Carrito import Carrito

from .form import *
from .Mindicator import Mindicador
from .models import *
from .models import Producto
from .serializers import *
from .utils import render_to_pdf


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

class ProductosViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializers
    renderer_classes = [JSONRenderer]

# AUTH
def login_view(request):
    aux = {
        'form' : AuthenticationForm()
    }
    if request.user.is_authenticated:
        messages.info(request, 'Ya estás logeado')
        return redirect(to="home")
    
    if request.method == 'POST':
        aux['form'] = AuthenticationForm(request, data=request.POST)
        if aux['form'].is_valid():
            username = aux['form'].cleaned_data.get('username')
            password = aux['form'].cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Inicio de sesión exitoso')
            return redirect(to="home")
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    
    return render(request, 'registration/login.html', aux)


def login_redirect(request):
    return redirect('login2')

def register(request):
    aux = {
        'form' : CustomUserCreationForm()
    }

    if request.user.is_authenticated:
        messages.info(request, 'Por favor, cierre sesión para registrarse.')
        return redirect(to="home")

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            #ASIGNAMOS UN GRUPO AL USUARIO CREADO
            grupo = Group.objects.get(name='Usuario')
            user.groups.add(grupo)
            # MENSAJE
            messages.success(request, 'Usuario Registrado')    
            # AUTENTICA Y LOGEA
            user = authenticate(request=request, username=formulario.cleaned_data['username'],password=formulario.cleaned_data['password1'])
            login(request, user)
            # LO MANDA A UNA PAGINA
            return redirect(to="home")
        else:
            aux['form'] = formulario
    return render(request, 'registration/register.html', aux)

def logout_view(request):
    logout(request)
    return redirect(to="home")

def account_locked(request):
    aux = {
        'LOCKOUT_TIME': int(settings.AXES_COOLOFF_TIME.total_seconds() // 60)
    }
    return render(request, 'registration/account_locked.html', aux)

# RECUPERAR CONTRASEÑA Y CAMBIAR
def recuperar_contrasena(request):
    return render(request, 'registration/recuperar_contrasena.html')

def cambiar_clave(request):
    return render(request, 'registration/cambiar_clave.html')


#UTILIZAMOS LOS VIEWSET PARA MANEJAR LAS SOLICITUDES HTTP (GET,POST,PUT,DELETE)
class VehiculoViewset(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer

# PAGINAS
def home(request):
    vehiculos = Vehiculo.objects.all()
    aux = {
        'lista' : vehiculos
    }
    return render(request, 'core/pages/home.html', aux)

def about(request):
    aux = {
        'breadcrumb' : {
            'title' : 'Acerca de Nosotros',
            'links' : ['Acerca de Nosotros']
        }
    }
    return render(request, 'core/pages/about.html', aux)

def agendar_hora(request):
    return render(request, 'core/pages/agendar_hora.html')

@login_required
def contactos(request):
    aux = {
        'breadcrumb' : {
            'title' : 'Contáctenos',
            'links' : ['Contáctenos']
        },
        'form' : ContactForm()
    }
    if request.method == "POST":
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            message = form.cleaned_data['message']

            EmailMessage(
                'Contact Form Submission from {}'.format(name),
                message,
                'form-response@example.com', # Send from (your website)
                [settings.EMAIL_HOST_USER], # Send to (your admin email)
                [],
                reply_to=[email] # Email from the form to get back to
            ).send()
            messages.success(request, 'Se ha enviado tu correo.')
            return redirect('contactos')
        else:
            messages.error(request, 'Por favor, revisa los campos.')
            form = ContactForm(request.POST)

    return render(request, 'core/pages/contactos.html', aux)

def formulario(request):
    return render(request, 'core/pages/formulario.html')

#VEHÍCULOS
def vehiculos(request):
    busqueda = request.GET.get('buscar')
    vehiculos = Vehiculo.objects.all()

    #BUSQUEDA
    if busqueda:
        vehiculos = Vehiculo.objects.filter(
            Q(modelo__icontains = busqueda) |
            Q(cant_puertas__icontains = busqueda) |
            Q(cant_pasajeros__icontains = busqueda) |
            Q(transmision__icontains = busqueda) |
            Q(capacidad__icontains = busqueda)
        )
    aux = {
        'lista' : vehiculos,
        'breadcrumb' : {
            'title' : 'Listado de autos',
            'links' : ['Listado']
        },
        'busqueda': busqueda
    }
    return render(request, 'core/pages/vehiculos.html', aux)

def informacion_auto(request):
    return render(request, 'core/pages/informacion_auto.html')

def listado_autos(request):
    return render(request, 'core/pages/listado_autos.html')

# PRODUCTOS
def productos(request):
    busqueda = request.GET.get('buscar')
    productos = Producto.objects.all()
    #BUSQUEDA
    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre__icontains = busqueda)
        )

    # PAGINADOR
    paginator = Paginator(productos, 9) # MUESTRA 10 DATOS
    page_number = request.GET.get('page') # OBTENEMOS LA PAGINA
    page_obj = paginator.get_page(page_number)
    aux = {
        'page_obj' : page_obj,
        'busqueda': busqueda
    }

    return render(request, 'core/pages/productos.html',aux)

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    messages.success(request, 'Producto agregado al carrito')
    return redirect("productos")

# CARRITO
def carrito(request):
    productos = Producto.objects.all()

    if request.method == "POST":
        carrito = Carrito(request)
        producto_id = request.POST.get('product_id')
        cantidad = request.POST.get('quantity')
        producto = Producto.objects.get(id=producto_id)
        carrito.establecer(producto, cantidad)

    return render(request, 'core/pages/carrito.html', {'producto': productos})

def agregar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    messages.success(request, 'Producto eliminado del carrito')
    return redirect("carrito")

def restar_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    messages.success(request, 'Carrito limpiado')
    return redirect("carrito")

class SearchVehiclesView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('query', '')
        vehicles = Vehicle.objects.filter(name__istartswith=query)
        results = list(vehicles.values('name', 'other_field'))
        return JsonResponse(results, safe=False)

#LISTADO DE PRODUCTOS PDF, CON LA CLASSE CARRITOCOMPLETAR
def carrito_completar(request):
    body = json.loads(request.body)
    productos = body['items']
    total = body['total']
    total_usd = body['total_usd']
    aux = {
        'productos': productos,
        'total': total,
        'total_usd': total_usd
    }
    # registrar en el modelo de ventas
    ventas = Venta.objects.create(total=total, productos=productos, usuario=request.user)
    ventas.save()
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('compra')

def comprar(request):
    return render(request, 'core/pages/compra.html')