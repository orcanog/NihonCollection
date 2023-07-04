from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def accueil(request):
    return render(request, 'Collection/templates/accueil.html')

def connexion(request):
    return render(request, 'Collection/templates/connexion.html')

def favori(request):
    return render(request, 'Collection/templates/favori.html')

def recherche(request):
    return render(request, 'Collection/templates/recherche.html')