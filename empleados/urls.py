from django.urls import path

from . import views

app_name = 'empleados'

urlpatterns = [
    path('', views.home, name='home'),
]
