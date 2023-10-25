from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)  # Agrega un campo para el nombre de usuario

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('username',)  # Incluye el campo 'username' en el formulario de registro
