from django.db import models


class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Empleado(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateField()
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='empleados')

    class Meta:
        ordering = ['apellidos', 'nombres']

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
