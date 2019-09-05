from django.db import models
from ckeditor.fields import RichTextField

class Categoria(models.Model):
    nombre = models.CharField('Nombre de la categoria', max_length=100, blank=False, null=False)
    estado = models.BooleanField('Categoria Activada/Desactivada', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre']

    def __str__(self):
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

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombre)

class Post(models.Model):
    titulo = models.CharField('Titulo', max_length=100, blank=False, null=False)
    slug = models.CharField('Slug', max_length=200, blank=False, null=False)
    descripcion = models.CharField('Descripcion', max_length=200, blank=False, null=False)
    contenido = RichTextField('Contenido')
    imagen = models.URLField('Url de la imagen', max_length=200, blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion = models.DateField('Fecha de creacion', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
