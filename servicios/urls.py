from django.urls import path
from . import views
#importamos las configuraciones para imagenes
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.servicios, name='servicios'),
]

