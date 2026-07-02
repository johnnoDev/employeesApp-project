from django.urls import path

from . import views_fbv as views

app_name = 'fbv'

urlpatterns = [
    path('cargos/', views.cargo_list, name='cargo_list'),
    path('cargos/nuevo/', views.cargo_create, name='cargo_create'),
    path('cargos/<int:pk>/editar/', views.cargo_update, name='cargo_update'),
    path('cargos/<int:pk>/eliminar/', views.cargo_delete, name='cargo_delete'),

    path('empleados/', views.empleado_list, name='empleado_list'),
    path('empleados/nuevo/', views.empleado_create, name='empleado_create'),
    path('empleados/<int:pk>/editar/', views.empleado_update, name='empleado_update'),
    path('empleados/<int:pk>/eliminar/', views.empleado_delete, name='empleado_delete'),
]
