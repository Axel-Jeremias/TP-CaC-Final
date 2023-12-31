"""
URL configuration for MasterFrame project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import IndexPage, FAQPage, CarteleraPage, ContactoPage, NotFoundView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", IndexPage.as_view(), name="inicio"),
    path("servicios", FAQPage.as_view(), name="servicios"),
    path("contacto", ContactoPage.as_view(), name="contacto"),
    path("cartelera", CarteleraPage.as_view(), name="cartelera"),
    path("peliculas/", include("app_peliculas.urls"))
]

handler404 = NotFoundView.as_view()
