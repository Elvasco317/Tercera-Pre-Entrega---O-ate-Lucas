from django.urls import path
from appentrega3.views import *


urlpatterns = [
    path('', index, name = "index"),
    path("cursos/", cursos, name = "cursos"),
    path("estudiantes/", estudiantes, name = "estudiantes"),
    path("profesores/", profesores, name = "profesores"),
    path("busca_curso/", busca_curso, name="busca_curso"),
    path('busqueda/', busqueda, name="busqueda"),
    path('buscar/', buscar, name="buscar"),
    path('resultadobusqueda/', resultadobusqueda, name="resultadobusqueda"),
    path('Error_al_buscar/', Error_al_buscar, name="Error_al_buscar"),
]