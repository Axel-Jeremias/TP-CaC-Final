from django.urls import path

from .views import PeliculasListView, PeliculasDetailView, PeliculasCreateView, PeliculasUpdateView, PeliculasDeleteView

app_name = "peliculas"

urlpatterns = [
    path("", PeliculasListView.as_view(), name="all"),
    path("crear/", PeliculasCreateView.as_view(), name="crear"),
    path("<int:pk>/detalles/", PeliculasDetailView.as_view(), name="detalles"),
    path("<int:pk>/editar/", PeliculasUpdateView.as_view(), name="editar"),
    path("<int:pk>/eliminar/", PeliculasDeleteView.as_view(), name="eliminar")
]
