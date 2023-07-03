from django.views.generic import TemplateView
from Views import connexion

class ConnexionView(TemplateView):
    template_name = "connexion.html"