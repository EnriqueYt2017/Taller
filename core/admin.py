from admin_confirm import AdminConfirmMixin
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


class VehiculoModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['modelo', 'marca', 'propietario', 'cant_puertas', 'cant_pasajeros', 'transmision', 'capacidad', 'velo_maxima', 'image']

class MarcaModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['descripcion']

class MantenimientoModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['fecha_revision', 'descripcion']

class AgendarHoraModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['nombre', 'email', 'capacidad', 'servicio']

class ProductoModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['nombre', 'categoria', 'precio', 'image']

class VentaModelAdmin(AdminConfirmMixin, ModelAdmin):
    confirm_change = True
    confirmation_fields = ['fecha', 'total', 'productos', 'usuario']

# Register your models here.
admin.site.register(Vehiculo, VehiculoModelAdmin)
admin.site.register(Marca, MarcaModelAdmin)
admin.site.register(Mantenimiento, MantenimientoModelAdmin)
admin.site.register(AgendarHora, AgendarHoraModelAdmin)
admin.site.register(Producto, ProductoModelAdmin)
admin.site.register(Venta, VentaModelAdmin)