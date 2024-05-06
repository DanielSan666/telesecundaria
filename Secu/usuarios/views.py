from django.shortcuts import render
from usuarios.models import User
# Create your views here.


def Usuarios(request):
    superusuario = User.objects.filter(is_superuser=True).first()
    return render(request, "usuarios.html", {'superusuario':superusuario})
