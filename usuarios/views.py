from django.shortcuts import render, redirect
from usuarios.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages

# Create your views here.

def Usuarios(request):
    usuarios_registrados = User.objects.all().prefetch_related('groups')
    return render(request, "usuarios.html", {'usuarios': usuarios_registrados})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()  # Guarda el usuario antes de asignar el grupo
            tipo_usuario = form.cleaned_data['tipo_usuario']
            if tipo_usuario == 'Control':
                group = Group.objects.get(name='Control')
                user.groups.add(group)
                messages.success(request, "Usuario registrado exitosamente")
                return redirect('Crear_Control')
            elif tipo_usuario == 'Profesor':
                group = Group.objects.get(name='Profesor')
                user.groups.add(group)
                messages.success(request, "Usuario registrado exitosamente")
                return redirect('create_profesor')
            else:
                group = Group.objects.get(name='Alumno')
                user.groups.add(group)
                messages.success(request, "Usuario registrado exitosamente")
                return redirect('create_alumnos')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})


    