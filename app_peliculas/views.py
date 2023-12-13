from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.db.models.query_utils import Q

from .models import Pelicula

#Revisar por las dudas


class PeliculasBaseView(View):
    template_name = 'peliculas.html'
    model = Pelicula
    fields = '__all__'
    success_url = reverse_lazy('peliculas:all')


class PeliculasListView(PeliculasBaseView, ListView):
    paginate_by = 15

    def get_queryset(self):
        queryset = super().get_queryset()
        parametros_url = self.request.GET.dict()

        filtros = Q()

        if "titulo" in parametros_url:
            filtros &= Q(titulo__istartswith=parametros_url["titulo"])
        if "director" in parametros_url:
            filtros &= Q(director__istartswith=parametros_url["director"])
        if "genero" in parametros_url:
            filtros &= Q(genero__iexact=parametros_url["genero"])
        if "año" in parametros_url:
            filtros &= Q(año__exact=parametros_url["año"])
        if "pais" in parametros_url:
            filtros &= Q(pais__iexact=parametros_url["pais"])
        if "lenguaje" in parametros_url:
            filtros &= Q(lenguaje__iexact=parametros_url["lenguaje"])

        return queryset.filter(filtros).order_by("id")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        parametros = self.request.GET.copy()

        if 'page' in parametros:
            del parametros['page']

        context['parametros'] = parametros.urlencode()

        return context


class PeliculasDetailView(PeliculasBaseView, DetailView):
    template_name = "peliculas_detalles.html"


class PeliculasCreateView(PeliculasBaseView, CreateView):
    template_name = "peliculas_creacion.html"
    extra_context = {
        "tipo": "Crear"
    }


class PeliculasUpdateView(PeliculasBaseView, UpdateView):
    template_name = "peliculas_creacion.html"
    extra_context = {
        "tipo": "Actualizar"
    }


class PeliculasDeleteView(PeliculasBaseView, DeleteView):
    template_name = "peliculas_eliminar.html"
