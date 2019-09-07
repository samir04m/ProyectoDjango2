from django.shortcuts import render, redirect, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from .forms import AutorForm
from .models import Autor

class Inicio(TemplateView):
    template_name = 'index.html'

class ListadoAutor(ListView):
    model = Autor
    template_name = 'libro/listar_autor.html'
    context_object_name = 'autores'
    queryset = Autor.objects.filter(estado = True)

class ActualizarAutor(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

class EliminarAutor(DeleteView):
    model = Autor

    def post(self,request,pk,*args,**kwargs):
        object = Autor.objects.get(id = pk)
        object.estado = False
        object.save()
        return redirect('libro:listar_autor')
