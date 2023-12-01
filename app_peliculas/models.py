from django.db import models
from django.core.validators import MinValueValidator

class Peliculas(models.model):
	DRAMA = 'Drama'
	COMEDIA = 'Comedia'
	HORROR = 'Horror'
	FANTASIA = 'Fantasia'
	ACCION = 'Accion'
	THRILLER = 'Thriller'
	ROMANCE = 'Romance'
	MISTERIO = 'Misterio'

	OPCIONES_GENERO = [
		(DRAMA, 'Drama'),
		(COMEDIA, 'Comedia'),
		(HORROR, 'Horror'),
		(FANTASIA, 'Fantasia'),
		(ACCION, 'Acción'),
		(THRILLER, 'Thriller'),
		(ROMANCE, 'Romance'),
		(MISTERIO, 'Misterio'),
	]

	OPCIONES_AÑOS = [(a, a) for a in range(1888, 2024)]

	nombre = models.CharField(max_length=100)
	año = models.IntegerField(choices=OPCIONES_AÑOS)
	genero = models.CharField(max_length=10, choices=OPCIONES_GENERO)
	lenguaje = models.CharField(max_length=30)
	pais = models.CharField(max_length=30)
	trailer = models.URLField(help_text="URL del trailer de la pelicula", blank=True)
	duracion = models.PositiveSmallIntegerField(help_text="Duración de la pelicula en minutos", validators=[MinValueValidator(45)])
	sinopsis = models.TextField()

	def __str__(self):
		return f"{self.nombre}, una pelicula de {self.get_genero_display} lanzada en {self.año}"
	
	def get_fields(self):
		return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
