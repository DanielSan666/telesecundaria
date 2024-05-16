from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usuarios.models import User


class CustomUserCreationForm(UserCreationForm):
    TIPO_USUARIO_CHOICES = [
        ('Control', 'Control'),
        ('Profesor', 'Profesor'),
        ('Alumno', 'Alumno'),
    ]
    
    tipo_usuario = forms.ChoiceField(choices=TIPO_USUARIO_CHOICES)
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'tipo_usuario')
