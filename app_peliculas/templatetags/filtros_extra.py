import re
import requests

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter
@stringfilter
def youtube_embed(link: str) -> str:
	"""
	Convierte un link de Youtube en un link embed para los iframes
	"youtube-nocookie" es usado para evitar los cookies de YT
	
	>>> youtube_embed("https://www.youtube.com/watch?v=cqGjhVJWtEg")
	"https://www.youtube-nocookie.com/embed/cqGjhVJWtEg"
	"""

	yt_id = re.search(r"(?:\?v=|\.be\/)([\w-]{11})", link)

	if yt_id.group(1):
		return 'https://www.youtube-nocookie.com/embed/' + yt_id.group(1)
	
	return link


@register.filter
@stringfilter
def es_video_youtube(link: str) -> bool:
	"""
	Verifica que un string sea un video de youtube
	
	>>> es_video_youtube("https://www.youtube.com/watch?v=cqGjhVJWtEg")
	True
	
	>>> es_video_youtube("https://www.dailymotion.com/video/x8gecdo")
	False
	"""

	yt_video_regex = re.compile(r"(?:youtu)(?:.be|be\.com)\/(?:watch\?v=|embed/)?[\w-]{11}", re.I)

	if yt_video_regex.search(link):
		return True

	return False


@register.filter
def duracion_string(minutos: int) -> str:
	"""
	Convierte minutos en un string con las horas y minutos
	
	>>> duracion_string(65)
	"1 hora 5 minutos"

	>>> duracion_string(54)
	"54 minutos"

	>>> duracion_string(120)
	"2 horas"
	"""

	horas, restante = divmod(minutos, 60)

	if horas:
		horas_string = f"{horas} hora{'s' if horas > 1 else ''}"
	else:
		horas_string = ""

	if restante:
		minutos_string = f"{restante} minuto{'s' if restante > 1 else ''}"
	else:
		minutos_string = ""

	return f"{horas_string} {minutos_string}".strip()


@register.filter
@stringfilter
def es_imagen_y_disponible(url: str) -> bool:
	"""
	Verifica que el link lleve a una imagen y esté disponible

	>>> es_imagen_y_disponible(https://www.example.com/portada.jpg)
	True
	>>> es_imagen_y_disponible(https://www.example.com/video.mp4)
	False
	"""

	formatos_imagenes = ("image/png", "image/jpeg", "image/jpg")

	r = requests.head(url)

	if r.headers["content-type"] in formatos_imagenes:
		return True

	return False
