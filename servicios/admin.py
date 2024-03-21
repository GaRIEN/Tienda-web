from django.contrib import admin
from .models import Servicios

# Register your models here.

#creamos una clase para poder mostrar la fecha que se va ingresar automatico
# class servicioAdmin(admin.ModelAdmin):
#     readonly_fields=('creadted', 'update')
    
    
#con esto agrego al panel del adminstrador
admin.site.register(Servicios)