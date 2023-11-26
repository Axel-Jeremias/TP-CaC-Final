from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = "index.html"

class FAQPage(TemplateView):
    template_name = "servicios.html"

class ContactoPage(TemplateView):
    template_name = "contacto.html"

class CarteleraPage(TemplateView):
    template_name = "cartelera.html"