from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import *

def home(request):
    queryset = request.GET.get('buscar')
    posts = Post.objects.filter(estado=True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
        
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {"posts":posts})

def generales(request):
    posts = Post.objects.filter(estado=True,
                                categoria=Categoria.objects.get(nombre__iexact='Tecnologia'))
    return render(request, 'generales.html', {"posts":posts})

def detallePost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {"post":post})
