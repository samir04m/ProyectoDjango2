from django.db import models


class Categoria(models.Model):
    nombre = models.CharField('Nombre de la categoria', max_length=100, blank=False, null=False)
    estado = models.BooleanField('Categoria Activada/Desactivada', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

    def __srt__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField('Nombre de autor', max_length=100, blank=False, null=False)
    apellidos = models.CharField('Apellidos', max_length=100, blank=False, null=False)
    correo = models.EmailField('Correo', blank=True, null=True)
    facebook = models.URLField('Facebook', blank=True, null=True)
    twitter = models.URLField('Twitter', blank=True, null=True)
    instagram = models.URLField('instagram', blank=True, null=True)
    web = models.URLField('Web', blank=True, null=True)
    estado = models.BooleanField('Categoria Activada/Desactivada', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __srt__(self):
        return "{0},{1}".format(self.apellidos, self.nombre)
