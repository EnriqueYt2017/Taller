from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import redirect, render

from core.models import *

from .form import *
from .models import *

from .utils import render_to_pdf
from django.views.generic import View
from django.http import HttpResponse


# Create your views here.
@permission_required('core.view_dashboard')
def dashboard(request):
    aux = {
        'segment': 'index'
    }
    
    return render(request, 'dashboard/pages/index.html', aux)

# Usuarios
@permission_required('auth.view_user')
def usuarios(request):
    users = User.objects.all()
    # PAGINADOR
    paginator = Paginator(users, 10) # MUESTRA 10 DATOS
    page_number = request.GET.get('page') # OBTENEMOS LA PAGINA
    page_obj = paginator.get_page(page_number)
    aux = {
        'segment': 'usuarios',
        'page_obj': page_obj
    }
    
    return render(request, 'dashboard/pages/usuarios/usuarios.html', aux)

@permission_required('auth.add_user')
def agregar_usuario(request):
    aux = {
        'segment': 'usuarios',
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request, 'Usuario agregado')
        else:
            aux['form'] = formulario
            messages.error(request, 'Error al agregar el usuario')
    
    return render(request, 'dashboard/pages/usuarios/agregar_usuario.html', aux)

@permission_required('auth.change_user')
def editar_usuario(request, id):
    usuario = User.objects.get(id=id)
    aux = {
        'segment': 'usuarios',
        'form': CustomUserChangeForm(instance=usuario)
    }

    if request.method == 'POST':
        formulario = CustomUserChangeForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            usuario.groups.clear()
            usuario.groups.add(formulario.cleaned_data['group'])
            aux['form'] = formulario
            messages.success(request, 'Usuario modificado')
        else:
            aux['form'] = formulario
            messages.error(request, 'Error al modificar el usuario')
    
    return render(request, 'dashboard/pages/usuarios/editar_usuario.html', aux)

@permission_required('auth.delete_user')
def eliminar_usuario(request, id):
    usuario = User.objects.get(id=id)
    if usuario:
        usuario.delete()
        messages.success(request, 'Usuario eliminado')
        return redirect(to="dashboard-usuarios")
    else:
        messages.error(request, 'Error al eliminar el usuario')

# Productos
@permission_required('core.view_producto')
def productos(request):
    products = Producto.objects.all()
    # PAGINADOR
    paginator = Paginator(products, 10) # MUESTRA 10 DATOS
    page_number = request.GET.get('page') # OBTENEMOS LA PAGINA
    page_obj = paginator.get_page(page_number)
    aux = {
        'segment': 'productos',
        'page_obj': page_obj
    }
    
    return render(request, 'dashboard/pages/productos/productos.html', aux)

@permission_required('core.add_producto')
def agregar_producto(request):
    aux = {
        'segment': 'productos',
        'form': ProductosForm()
    }

    if request.method == 'POST':
        formulario = ProductosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request, 'Producto agregado')
        else:
            aux['form'] = formulario
            messages.error(request, 'Error al agregar el producto')
    
    return render(request, 'dashboard/pages/productos/agregar_producto.html', aux)

@permission_required('core.change_producto')
def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    aux = {
        'segment': 'productos',
        'form': ProductosForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductosForm(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request, 'Producto modificado')
        else:
            aux['form'] = formulario
            messages.error(request, 'Error al modificar el producto')
    
    return render(request, 'dashboard/pages/productos/editar_producto.html', aux)

@permission_required('core.delete_producto')
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if producto:
        producto.delete()
        messages.success(request, 'Producto eliminado')
        return redirect(to="dashboard-productos")
    else:
        messages.error(request, 'Error al eliminar el producto')

# Vehículos
@permission_required('core.view_vehiculo')
def vehiculos(request):
    products = Vehiculo.objects.all()
    # PAGINADOR
    paginator = Paginator(products, 10) # MUESTRA 10 DATOS
    page_number = request.GET.get('page') # OBTENEMOS LA PAGINA
    page_obj = paginator.get_page(page_number)
    aux = {
        'segment': 'vehiculos',
        'page_obj': page_obj
    }
    
    return render(request, 'dashboard/pages/vehiculos/vehiculos.html', aux)

@permission_required('core.add_vehiculo')
def agregar_vehiculo(request):
    aux = {
        'segment': 'vehiculos',
        'form': VehiculosForm()
    }

    if request.method == 'POST':
        formulario = VehiculosForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request, 'Vehículo agregado')
        else:
            aux['form'] = formulario
            messages.error(request, 'Error al agregar el vehículo')
    
    return render(request, 'dashboard/pages/vehiculos/agregar_vehiculo.html', aux)

@permission_required('core.change_vehiculo')
def editar_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    aux = {
        'segment': 'vehiculos',
        'form': VehiculosForm(instance=vehiculo)
    }

    if request.method == 'POST':
        formulario = VehiculosForm(data=request.POST, instance=vehiculo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request, 'Vehículo modificado')
        else:
            aux['form'] = formulario
            messages.error(request, 'Error al modificar el vehículo')
    
    return render(request, 'dashboard/pages/vehiculos/editar_vehiculo.html', aux)

@permission_required('core.delete_vehiculo')
def eliminar_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    if vehiculo:
        vehiculo.delete()
        messages.success(request, 'Vehículo eliminado')
        return redirect(to="dashboard-vehiculos")
    else:
        messages.error(request, 'Error al eliminar el vehículo')


def index(request):
    return render(request, 'dashboard/templates/index.html')

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        pdf = render_to_pdf('dashboard/templates/reports.html')
        return HttpResponse(pdf, content_type='application/pdf')