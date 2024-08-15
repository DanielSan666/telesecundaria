from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import logout
from api.form import *
from .models import *
# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def inicio(request):
    return render(request, "inicio.html")

def exit(request):
    logout(request)
    return redirect('/')

@login_required
def index(request):
    profesores = Profesores.objects.all()  # Inicializa 'profesor' con todos los profesores

    if request.method == "POST":
        if "create" in request.POST:
            grupo = request.POST.get("grupo")
            nombre_profesor = request.POST.get("nombre_profesor")
            nombre_materia = request.POST.get("nombre_materia")
            calificacion_1 = request.POST.get("calificacion_1")
            calificacion_2 = request.POST.get("calificacion_2")
            calificacion_3 = request.POST.get("calificacion_3")
            evaluacion_final = request.POST.get("evaluacion_final")
            calificacion_final = request.POST.get("calificacion_final")
            alumno_id = request.POST.get("alumno")
            alumno = Alumno.objects.get(id=alumno_id)
            profesor_id = request.POST.get("profesor")
            profesor = Profesores.objects.get(id=profesor_id)

            Calificaciones.objects.create(
                grupo=grupo,
                nombre_profesor=nombre_profesor,
                nombre_materia=nombre_materia,
                calificacion_1=calificacion_1,
                calificacion_2=calificacion_2,
                calificacion_3=calificacion_3,
                evaluacion_final=evaluacion_final,
                calificacion_final=calificacion_final,
                alumno=alumno,
                profesor=profesor
            )
            messages.success(request, "Calificación añadida exitosamente")

        elif "update" in request.POST:
            id = request.POST.get("id")
            grupo = request.POST.get("grupo")
            nombre_profesor = request.POST.get("nombre_profesor")
            nombre_materia = request.POST.get("nombre_materia")
            calificacion_1 = request.POST.get("calificacion_1")
            calificacion_2 = request.POST.get("calificacion_2")
            calificacion_3 = request.POST.get("calificacion_3")
            evaluacion_final = request.POST.get("evaluacion_final")
            calificacion_final = request.POST.get("calificacion_final")
            calificacion = Calificaciones.objects.get(id=id)
            calificacion.grupo = grupo
            calificacion.nombre_profesor = nombre_profesor
            calificacion.nombre_materia = nombre_materia
            calificacion.calificacion_1 = calificacion_1
            calificacion.calificacion_2 = calificacion_2
            calificacion.calificacion_3 = calificacion_3
            calificacion.evaluacion_final = evaluacion_final
            calificacion.calificacion_final = calificacion_final
            calificacion.save()
            messages.success(request, "Calificación actualizada exitosamente")

        elif "delete" in request.POST:
            id = request.POST.get("id")
            Calificaciones.objects.get(id=id).delete()
            messages.success(request, "Calificación eliminada exitosamente")

        elif "search" in request.POST:
            search_query = request.POST.get("query")
            calificaciones = Calificaciones.objects.filter(
                Q(grupo__icontains=search_query) | 
                Q(nombre_profesor__icontains=search_query) | 
                Q(nombre_materia__icontains=search_query)
            )
            context = {
                "calificaciones": calificaciones, 
                "search_query": search_query, 
                "alumnos": Alumno.objects.all(), 
                "profesores": profesores
            }
            return render(request, "index.html", context=context)

    calificaciones = Calificaciones.objects.all()
    alumnos = Alumno.objects.all()
    context = {
        "calificaciones": calificaciones,
        "alumnos": alumnos,
        "profesores": profesores,
        "search_query": ""
    }
    return render(request, "index.html", context=context)

@login_required
def create_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = AlumnoForm()
    return render(request, 'create_alumno.html', {'form': form})

@login_required
def create_profesor(request):
    if request.method == 'POST':
        form = ProfesoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ProfesoresForm()
    return render(request, 'create_profesor.html', {'form':form})

@login_required
def create_control(request):
    if request.method == 'POST':
        form = ControlForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = ControlForm()
    return render(request, 'create_control.html', {'form':form})