from django.shortcuts import render

# Create your views here.

def accueil(request):
    return render(request, 'Collection/templates/accueil.html')

def connexion(request):
    return render(request, 'Collection/templates/connexion.html')

def favori(request):
    return render(request, 'Collection/templates/favori.html')

def recherche(request):
    return render(request, 'Collection/templates/recherche.html')