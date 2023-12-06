from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView

from .models import Pelicula

#Revisar por las dudas


class PeliculasBaseView(View):
    template_name = 'peliculas.html'
    model = Pelicula
    fields = '__all__'
    success_url = reverse_lazy('peliculas:all')


class PeliculasListView(PeliculasBaseView, ListView):
    paginate_by = 10
    ordering = ["id"]


class PeliculasDetailView(PeliculasBaseView, DetailView):
    template_name = "peliculas_detalles.html"


class PeliculasCreateView(PeliculasBaseView, CreateView):
    template_name = "peliculas_creacion.html"
    extra_context = {
        "tipo": "Crear pelicula"
    }


class PeliculasUpdateView(PeliculasBaseView, UpdateView):
    template_name = "peliculas_creacion.html"
    extra_context = {
        "tipo": "Actualizar pelicula"
    }


class PeliculasDeleteView(PeliculasBaseView, DeleteView):
    template_name = "peliculas_eliminar.html"
    extra_context = {
        "tipo": "Borrar pelicula"
    }