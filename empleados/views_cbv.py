from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CargoForm, EmpleadoForm
from .models import Cargo, Empleado


# --- Cargo ---

class CargoListView(LoginRequiredMixin, ListView):
    model = Cargo
    template_name = 'empleados/cbv/cargo_list.html'
    context_object_name = 'cargos'


class CargoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'empleados/cbv/cargo_form.html'
    success_url = reverse_lazy('cbv:cargo_list')
    success_message = 'Cargo registrado correctamente.'
    extra_context = {'titulo': 'Registrar cargo'}


class CargoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'empleados/cbv/cargo_form.html'
    success_url = reverse_lazy('cbv:cargo_list')
    success_message = 'Cargo actualizado correctamente.'
    extra_context = {'titulo': 'Editar cargo'}


class CargoDeleteView(LoginRequiredMixin, DeleteView):
    model = Cargo
    template_name = 'empleados/cbv/cargo_confirm_delete.html'
    success_url = reverse_lazy('cbv:cargo_list')

    def form_valid(self, form):
        messages.success(self.request, 'Cargo eliminado correctamente.')
        return super().form_valid(form)


# --- Empleado ---

class EmpleadoListView(LoginRequiredMixin, ListView):
    model = Empleado
    template_name = 'empleados/cbv/empleado_list.html'
    context_object_name = 'empleados'
    queryset = Empleado.objects.select_related('cargo').all()


class EmpleadoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/cbv/empleado_form.html'
    success_url = reverse_lazy('cbv:empleado_list')
    success_message = 'Empleado registrado correctamente.'
    extra_context = {'titulo': 'Registrar empleado'}


class EmpleadoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/cbv/empleado_form.html'
    success_url = reverse_lazy('cbv:empleado_list')
    success_message = 'Empleado actualizado correctamente.'
    extra_context = {'titulo': 'Editar empleado'}


class EmpleadoDeleteView(LoginRequiredMixin, DeleteView):
    model = Empleado
    template_name = 'empleados/cbv/empleado_confirm_delete.html'
    success_url = reverse_lazy('cbv:empleado_list')

    def form_valid(self, form):
        messages.success(self.request, 'Empleado eliminado correctamente.')
        return super().form_valid(form)
