from django.shortcuts import render
from django.http import HttpResponse
from appentrega3.models import Cursos, Estudiantes, Profesores


def index(request):
    return render(request, "appentrega3/index.html")

def cursos(request):
    if request.method == "POST":

        print(f"\n\n{request.POST}\n\n")
        nombre = request.POST["nombre"]
        camada = request.POST["camada"] 
        nombre = Cursos(nombre=nombre, camada=camada)
        nombre.save()

    return render(request, "appentrega3/cursos.html")

def estudiantes(request):
    if request.method == "POST":

        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        email = request.POST["email"]
        nombre = Estudiantes(nombre=nombre, apellido=apellido, email=email)
        nombre.save()

    return render(request, "appentrega3/estudiantes.html")

def profesores(request):
    if request.method == "POST":

        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        email = request.POST["email"]
        nombre = Profesores(nombre=nombre, apellido=apellido, email=email)
        nombre.save()
    return render(request, "appentrega3/profesores.html")

def busca_curso(request):
    return render(request, "appentrega3/busca_curso.html")

def resultadobusqueda(request):
    return render(request, "appentrega3/resultadobusqueda.html")

def busqueda(request):
    return render(request, "appentrega3/buscar.html")

def Error_al_buscar(request): 
    return render(request,"appentrega3/Error_al_buscar.html")

def buscar(request):

    if request.GET['camada']:
        camada = request.GET['camada']
        cursos = Cursos.objects.filter(camada__icontains=camada)

        return render(request, "appentrega3/resultadobusqueda.html",{"cursos":cursos, "camada":camada})

    else:

        respuesta = render(request, "appentrega3/Error_al_buscar.html")

    return HttpResponse(respuesta)

