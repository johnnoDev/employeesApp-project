from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CargoForm, EmpleadoForm
from .models import Cargo, Empleado


# --- Cargo ---

def cargo_list(request):
    cargos = Cargo.objects.all()
    return render(request, 'empleados/fbv/cargo_list.html', {'cargos': cargos})


def cargo_create(request):
    if request.method == 'POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cargo registrado correctamente.')
            return redirect('fbv:cargo_list')
    else:
        form = CargoForm()
    return render(request, 'empleados/fbv/cargo_form.html', {'form': form, 'titulo': 'Registrar cargo'})


def cargo_update(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == 'POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cargo actualizado correctamente.')
            return redirect('fbv:cargo_list')
    else:
        form = CargoForm(instance=cargo)
    return render(request, 'empleados/fbv/cargo_form.html', {'form': form, 'titulo': 'Editar cargo'})


def cargo_delete(request, pk):
    cargo = get_object_or_404(Cargo, pk=pk)
    if request.method == 'POST':
        cargo.delete()
        messages.success(request, 'Cargo eliminado correctamente.')
        return redirect('fbv:cargo_list')
    return render(request, 'empleados/fbv/cargo_confirm_delete.html', {'cargo': cargo})


# --- Empleado ---

def empleado_list(request):
    empleados = Empleado.objects.select_related('cargo').all()
    return render(request, 'empleados/fbv/empleado_list.html', {'empleados': empleados})


def empleado_create(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado registrado correctamente.')
            return redirect('fbv:empleado_list')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/fbv/empleado_form.html', {'form': form, 'titulo': 'Registrar empleado'})


def empleado_update(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empleado actualizado correctamente.')
            return redirect('fbv:empleado_list')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/fbv/empleado_form.html', {'form': form, 'titulo': 'Editar empleado'})


def empleado_delete(request, pk):
    empleado = get_object_or_404(Empleado, pk=pk)
    if request.method == 'POST':
        empleado.delete()
        messages.success(request, 'Empleado eliminado correctamente.')
        return redirect('fbv:empleado_list')
    return render(request, 'empleados/fbv/empleado_confirm_delete.html', {'empleado': empleado})
