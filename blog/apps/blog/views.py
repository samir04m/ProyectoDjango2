from django.shortcuts import render
from .models import *

def home(request):
    posts = Post.objects.filter(estado=True)
    return render(request, 'index.html', {"posts":posts})

def generales(request):
    posts = Post.objects.filter(estado=True,
                                categoria=Categoria.objects.get(nombre='Tecnologia'))
    return render(request, 'generales.html', {"posts":posts})

def detallePost(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post.html', {"post":post})
