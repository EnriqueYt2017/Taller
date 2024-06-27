from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Vehiculo)
admin.site.register(Marca)
admin.site.register(Mantenimiento)
admin.site.register(AgendarHora)
admin.site.register(Producto)
admin.site.register(Venta)