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
from Collection import views
from Views import ConnexionView, FavoriView, RechercheView, MyView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('', MyView, name="accueil"),
    path('connexion/', ConnexionView.as_view(), name="connexion"),
    path('favori/', FavoriView.as_view(), name="favori"),
    path('recherche/', RechercheView.as_view(), name="recherche"),
    path("accounts/", include("django.contrib.auth.urls")),
   
]
