# Documentación del Proyecto Full Stack "MasterFrame"

Documentación del Trabajo Integrador Final Full Stack "MasterFrame" para el curso Desarrollo Full Stack Python del programa Codo a Codo

## Descripción del Proyecto

Un sitio web para acceder a la información sobre los cines Masterframe, consultar el catálogo, novedades, los últimos trailers, información importante, contactar a la empresa a través de un formulario, e interactuar con la base de datos de MySQL, en las cuales uno puede agregar, modificar, y eliminar películas.

El sitio web también permite filtrar la tabla de la base de datos con las películas a través de queries en la URL. Si uno accede a la página `peliculas/?genero=Acción`, la tabla solo mostrará las películas de Acción. Incluso se pueden usar múltiples queries al mismo tiempo, como por ejemplo `?genero=Comedia&año=2018`, que muestra las películas de Comedia lanzadas en el 2018.

## Tecnologías Utilizadas

- **Frontend**:
  - Frameworks: Vue, Bootstrap

- **Backend**:
  - Lenguaje de programación: Python
  - Frameworks: Django
  - Base de datos: MySQL

- **Deploy**:
  - PythonAnywhere

## Estructura del Proyecto

El proyecto cuenta con 4 carpetas principales:

* **static**, donde uno puede encontrar las imágenes, el CSS, y JS (este último además conteniendo los cores y componentes de Vue)
* **templates**, la cual contiene nuestra template base para todo el sitio web, las templates de Django no relacionados a la aplicación, y una template para customizar la página al recibir un Error 404
* **Masterframe**, donde podemos encontrar la configuración de nuestro proyecto de Django
* **app_peliculas**, que cuenta con la configuración de nuestra app de Django, sus respectivas templates (inclusive uno para editar la versión base de la documentación de la API de DRF), nuestro modelo, y templatetags, con nuestros filtros de Django personalizados.

Respecto a las páginas en si, en el sitio web uno puede visitar las siguientes páginas (nuevas en *itálica*):

* Inicio
  * Novedades
  * Trailers
* Cartelera
* Preguntas frecuentes
* *Películas*
  * *Detalles*
  * *Agregar / Editar*
  * *Eliminar*
* Contacto
* *API*

La página *películas* es la principal adición respecto al proyecto anterior de Front End, ya que, gracias al modelo MVT de Django, nos permite completa interacción con la base de datos y contar con páginas dinámicas a través de las templates.

## Integrantes del Proyecto

* Marcelo Adrián Sosa
* Axel Jeremías
