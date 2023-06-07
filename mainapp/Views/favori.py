from django.views.generic import TemplateView

class FavView(TemplateView):
    template_name = "favorite.html"