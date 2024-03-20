
from django.contrib import admin
from django.urls import path, include
from ProyectoWebapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('ProyectoWebapp.urls')),
]

