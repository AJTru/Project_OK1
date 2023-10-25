from django.contrib.auth import login
from .forms import CustomUserCreationForm  # Asegúrate de importar el formulario personalizado
from .models import User
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Inicia sesión al usuario automáticamente
            return redirect('página_de_inicio')  # Redirige a la página de inicio o a donde desees
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})
