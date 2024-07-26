# models.py en tu aplicación gestionusuario
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    RUT_MAX_LENGTH = 12
    CARGO_CHOICES = [
        ('SUPERVISOR', 'Supervisor'),
        ('TRABAJADOR', 'Trabajador'),
        ('GERENTE', 'Gerente'),
        ('GERENTE_GENERAL', 'Gerente General'),
    ]

    rut = models.CharField(max_length=RUT_MAX_LENGTH, unique=True)
    cargo = models.CharField(max_length=20, choices=CARGO_CHOICES)

    def __str__(self):
        return self.username

class Division(models.Model):
    nombre = models.CharField(max_length=100)
    gerente_general = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'cargo': 'GERENTE_GENERAL'})

    def __str__(self):
        return self.nombre

class Area(models.Model):
    nombre = models.CharField(max_length=100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    gerente = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'cargo': 'GERENTE'})

    def __str__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'cargo': 'SUPERVISOR'})
    trabajadores = models.ManyToManyField(CustomUser, related_name='grupos', limit_choices_to={'cargo': 'TRABAJADOR'})

    def __str__(self):
        return self.nombre


class ART(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    fecha = models.DateField()
    cantidad_firmas = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"ART {self.id} - {self.grupo.nombre} - {self.fecha}"
    
# models.py en tu aplicación gestionusuario
class Firma(models.Model):
    art = models.ForeignKey(ART, on_delete=models.CASCADE)
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fecha_firma = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.art.id} - {self.fecha_firma}"
