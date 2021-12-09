from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellidoPa = models.CharField(max_length=30)
    correo = models.EmailField(blank=True,null=True)
    usuario = models.CharField(max_length=30)
    password = models.CharField("Contraseña (escoge una contraseña segura):",max_length=30)

    def __str__(self):
        return self.usuario