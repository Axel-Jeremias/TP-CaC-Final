from django.contrib import admin
from .models import Pelicula

@admin.register(Pelicula)
class PeliculasAdmin(admin.ModelAdmin):
    ...
