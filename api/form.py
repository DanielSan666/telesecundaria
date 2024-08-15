from django import forms
from api.models import *

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesoresForm(forms.ModelForm):
    class Meta:
        model =  Profesores
        fields = '__all__'

class ControlForm(forms.ModelForm):
    class Meta:
        model = Control
        fields = '__all__'

class CalificacionesForm(forms.ModelForm):
    class Meta:
        model = Calificaciones
        fields = '__all__'