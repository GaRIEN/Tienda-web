
from django.contrib import admin
from django.urls import path, include
from ProyectoWebapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #registrar la ruta de la app    
    path('', include('ProyectoWebapp.urls')),
    #registrar la ruta de la app    
    path('servicios/', include('servicios.urls')),

]

