from django.shortcuts import render, HttpResponse,redirect
from servicios.models import  Servicios
# Create your views here.
def home(request):
    return render(request, "proyectowebApp/home.html")

def servicios(request):
    servicios=Servicios.objects.all()
    print(servicios)
    return render(request, "proyectowebApp/servicios.html",{'servicios':servicios})

def tienda(request):
    return render(request, "proyectowebApp/tienda.html")

def blog(request):
    return render(request, "proyectowebApp/blog.html")

def contacto(request):
    return render(request, "proyectowebApp/contacto.html")
