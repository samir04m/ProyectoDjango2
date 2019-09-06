from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *

def home(request):
    posts = Post.objects.filter(estado=True)
    return render(request, 'index.html', {"posts":posts})

def generales(request):
    posts = Post.objects.filter(estado=True,
                                categoria=Categoria.objects.get(nombre__iexact='Tecnologia'))
    return render(request, 'generales.html', {"posts":posts})

def detallePost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {"post":post})
