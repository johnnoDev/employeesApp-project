from django.urls import path

from . import views_cbv as views

app_name = 'cbv'

urlpatterns = [
    path('cargos/', views.CargoListView.as_view(), name='cargo_list'),
    path('cargos/nuevo/', views.CargoCreateView.as_view(), name='cargo_create'),
    path('cargos/<int:pk>/editar/', views.CargoUpdateView.as_view(), name='cargo_update'),
    path('cargos/<int:pk>/eliminar/', views.CargoDeleteView.as_view(), name='cargo_delete'),

    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/nuevo/', views.EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/<int:pk>/editar/', views.EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleados/<int:pk>/eliminar/', views.EmpleadoDeleteView.as_view(), name='empleado_delete'),
]
