from rest_framework.serializers import ModelSerializer

from .models import Pelicula


class PeliculaSerializer(ModelSerializer):
    class Meta:
        model = Pelicula
        fields = "__all__"
