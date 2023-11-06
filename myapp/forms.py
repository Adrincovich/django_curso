from django import forms
from django.forms import ModelForm
from .models import Curso, Profesor

# SIN EL MODEL

# class FormularioCurso(forms.Form):
#     nombre = forms.CharField(label="Nombre", max_length=128)
#     inscriptos = forms.IntegerField(label="Inscriptos")
#     turnos = (
#         (1, "Mañana"),
#         (2, "Tarde"),
#         (3, "Noche")
#     )
#     turno = forms.ChoiceField(label="Turno", choices=turnos)

# CON MODEL

class FormularioCurso(ModelForm):
    class Meta:
        model = Curso
        fields = ("nombre", "inscriptos", "turno", "profesor")
        

