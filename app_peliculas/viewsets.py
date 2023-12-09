from rest_framework.viewsets import ModelViewSet

from .models import Pelicula
from .serializers import PeliculaSerializer


class PeliculaViewSet(ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
