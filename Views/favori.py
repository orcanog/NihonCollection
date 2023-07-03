from django.views.generic import TemplateView
from Views import favori

class FavoriView(TemplateView):
    template_name = "favori.html"