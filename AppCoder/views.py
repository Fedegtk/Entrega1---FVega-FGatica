from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *
# Create your views here.
def home(request):
    return render(request, "home.html")

def cursos(request):
    if request.method == "POST":
        curso = Curso(materia = request.POST["materia"], numero = request.POST["numero"],)
        curso.save()
        return render(request, "home.html")
    return render(request, "cursos.html")

def estudiantes(request):
    if request.method == "POST":
        estudiante = Estudiante(nombre = request.POST["nombre"], apellido = request.POST["apellido"], email = request.POST["email"],)
        estudiante.save()
        return render(request, "home.html")
    return render(request, "estudiantes.html")
    
def buscar_estudiante(request):
    if request.GET["email"]:
        email = request.GET["email"]
        estudiantes = Estudiante.objects.filter(email__icontains = email) 
        return render(request, "estudiantes.html", {"estudiantes": estudiantes})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def buscar_curso(request):
    if request.GET["numero"]:
        numero = request.GET["numero"]
        cursos = Curso.objects.filter(numero__icontains = numero) 
        return render(request, "cursos.html", {"cursos": cursos})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def buscar_profesor(request):
    if request.GET["email"]:
        email = request.GET["email"]
        profesores = Profesor.objects.filter(email__icontains = email) 
        return render(request, "profesores.html", {"profesores": profesores})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def profesores(request):
    if request.method == "POST":
        profesor = Profesor(nombre = request.POST["nombre"], apellido = request.POST["apellido"], email = request.POST["email"], area = request.POST["area"],)
        profesor.save()
        return render(request, "home.html")
    return render(request, "profesores.html")