"""
URL configuration for NihonCollection project.

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
from Views import ConnexionView, MyView, SignUpView, favorites, anime_detail, search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MyView, name="accueil"),
    path('connexion/', ConnexionView.as_view(), name="connexion"),
    path('favori/', favorites.animeFavoris, name="favori"),
    path('creation/', SignUpView.as_view(), name="creation"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('ajouter_aux_favoris/', favorites.ajouter_aux_favoris, name='addFavoris'),
    path('supprimer_des_favoris/', favorites.supprimer_des_favoris, name='supprimer_des_favoris'),
    path('anime/<int:anime_id>/', anime_detail, name="detail"),
    path('recherche/', search, name='recherche')
]
