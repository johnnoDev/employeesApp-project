from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import RegistroForm


def home(request):
    return render(request, 'empleados/home.html')


def signup(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cuenta creada correctamente. ¡Bienvenido!')
            return redirect('empleados:home')
    else:
        form = RegistroForm()
    return render(request, 'registration/signup.html', {'form': form})
