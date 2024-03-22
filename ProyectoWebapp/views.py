from django.shortcuts import render, HttpResponse,redirect
# Create your views here.
def home(request):
    return render(request, "proyectowebApp/home.html")


def tienda(request):
    return render(request, "proyectowebApp/tienda.html")

def blog(request):
    return render(request, "proyectowebApp/blog.html")

def contacto(request):
    return render(request, "proyectowebApp/contacto.html")
