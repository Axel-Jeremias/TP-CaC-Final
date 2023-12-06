from django.contrib import admin
from django.urls import path , include


from .views import      PeliculasListView   \
                    ,   PeliculasDetailView \
                    ,   PeliculasCreateView \
                    ,   PeliculasUpdateView \
                    ,   PeliculasDeleteView

app_name = "peliculas"

urlpatterns = [
    path("", PeliculasListView.as_view(), name="all"),
    path("create/", PeliculasCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", PeliculasDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", PeliculasUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", PeliculasDeleteView.as_view(), name="delete")

]