from django import forms
from .models import Profesor

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = '__all__'  # O especifica los campos que deseas incluir en el formulario