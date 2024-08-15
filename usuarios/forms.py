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
    matricula = forms.CharField(max_length=10, required=False)
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'tipo_usuario')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.tipo_usuario = self.cleaned_data['tipo_usuario']
        user.matricula = self.cleaned_data['matricula']
        
        if commit:
            user.save()
        return user
