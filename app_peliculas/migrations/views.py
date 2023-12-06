from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from .models import Peliculas

#Revisar por las dudas.

class PeliculasBaseView(View):
    template_name = "index.html"
    model = Peliculas
    fields = '__all__'
    succes_url = reverse_lazy('Peliculas:all')

class PeliculasListView(PeliculasBaseView, ListView):
     """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS VINOS
    """

class PeliculasDetailView(PeliculasBaseView,DetailView):
    template_name = "pelicula_detail.html"

class PeliculasCreateView(PeliculasBaseView,CreateView):
    template_name = "pelicula_create.html"
    extra_context = {
        "tipo": "Crear pelicula"
    }

class PeliculasUpdateView(PeliculasBaseView,UpdateView):
    template_name = "pelicula_create.html"
    extra_context = {
        "tipo": "Actualizar pelicula"
    }

class PeliculasDeleteView(PeliculasBaseView,DeleteView):
    template_name = "pelicula_delete.html"
    extra_context = {
        "tipo": "Borrar pelicula"
    }