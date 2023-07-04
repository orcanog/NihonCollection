from django.views.generic import TemplateView


class RechercheView(TemplateView):
    template_name = "recherche.html"