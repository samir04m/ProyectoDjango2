from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=200, blank=False, null=False)
    nacionalidad = models.CharField(max_length=200, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.BooleanField('Estado', default = True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField('Titulo', max_length=200, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha de Publicación', blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    autor_id = models.ManyToManyField(Autor)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
