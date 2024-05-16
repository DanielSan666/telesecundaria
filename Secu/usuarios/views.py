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
            user = form.save(commit=False)  # No guardes el usuario aún
            tipo_usuario = form.cleaned_data['tipo_usuario']  # Obtén el tipo de usuario del formulario
            if tipo_usuario == 'Control':
                group = Group.objects.get(name='Control')
            elif tipo_usuario == 'Profesor':
                group = Group.objects.get(name='Profesor')
            else:
                group = Group.objects.get(name='Alumno')
            user.save() 
            messages.success(request, "Usuarrio registrado exitosamente") # Guarda el usuario después de asignar el grupo
            user.groups.add(group)
            return redirect('login')  # Redirige a una página de registro exitoso
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})