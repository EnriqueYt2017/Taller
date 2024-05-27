from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class VehiculoForm(ModelForm):

    class Meta:
        model = Vehiculo
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email']

class EmpleadoForm(ModelForm):

    class Meta:
        model = Empleado
        fields = '__all__'

class GeneroForm(ModelForm):

    class Meta:
        model = Genero
        fields = '__all__'

class MantenimientoForm(ModelForm):

    class Meta:
        model = Mantenimiento
        fields = '__all__'

class TipoEmpleadoForm(ModelForm):

    class Meta:
        model = TipoEmpleado
        fields = '__all__'



