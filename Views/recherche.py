from django.views.generic import TemplateView
from Views import recherche

class RechercheView(TemplateView):
    template_name = "recherche.html"