from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('generales/', generales, name='generales'),
    path('post/<slug:slug>/', detallePost, name='detallePost'), #(importante colocar al final de las urls)
]
