from django.shortcuts import render
from django.http import HttpResponse
import requests

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
<<<<<<< HEAD
    return HttpResponse('<h1>PAGE RECHERCHE</h1>')
    #return render(request, 'Collection/templates/recherche.html')


=======
    return render(request, 'Collection/templates/recherche.html')
>>>>>>> 9330bc9e47ba77bfaa72af1acd626bc53a0d6ddd
