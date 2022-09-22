from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', home),
    path('cursos/', cursos),
    path('estudiantes/', estudiantes),
    path('profesores/', profesores),
    path('buscar_estudiante/', buscar_estudiante),
    path('buscar_curso/', buscar_curso),
    path('buscar_profesor/', buscar_profesor),
]
