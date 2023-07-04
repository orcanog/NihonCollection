from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def accueil(request):
    return HttpResponse('<h1>PAGE ACCUEIL</h1>')
    #return render(request, 'Collection/templates/accueil.html')

def connexion(request):
    return HttpResponse('<h1>PAGE CONNEXION</h1>')
    #return render(request, 'Collection/templates/connexion.html')

def favori(request):
    return HttpResponse('<h1>PAGE FAVORI</h1>')
    #return render(request, 'Collection/templates/favori.html')

def recherche(request):
    return HttpResponse('<h1>PAGE RECHERCHE</h1>')
    #return render(request, 'Collection/templates/recherche.html')


