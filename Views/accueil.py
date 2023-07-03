from django.views.generic import TemplateView
from Views import accueil

class HomeView(TemplateView):
    template_name = "accueil.html"