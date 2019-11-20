from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField('Nombre de la empresa', max_length=150, unique=True)
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField('Nombre de usuario', max_length=150, unique=True)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Lista(models.Model):
    id_usuarios = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Lista'
        verbose_name_plural = 'Listas'
