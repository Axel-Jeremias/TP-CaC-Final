from django.contrib import admin
from .models import Peliculas

@admin.register(Peliculas)
class PeliculasAdmin(admin.ModelAdmin):
    ...
