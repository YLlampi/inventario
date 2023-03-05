from django.db import models
from datetime import datetime


# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']


class Employee(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    names = models.CharField(max_length=100, verbose_name='Nombres')
    dni = models.CharField(max_length=8, unique=True, verbose_name='DNI')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.0, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    # gender = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return f'{self.names}'

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        # db_table = 'empleado'
        ordering = ['id']
