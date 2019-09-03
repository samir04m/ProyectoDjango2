from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=200, blank=False, null=False)
    nacionalidad = models.CharField(max_length=200, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
