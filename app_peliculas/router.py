from rest_framework import routers
from .viewsets import PeliculaViewSet


router = routers.SimpleRouter()

router.register("api", PeliculaViewSet)
