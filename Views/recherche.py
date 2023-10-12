import requests
from django.shortcuts import render

def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        response = requests.get(f'https://kitsu.io/api/edge/anime?filter[text]={query}')
        data = response.json()
        results = data['data']

        context = {
            'recherche_data': results # On passe les résultats de recherche au template
        }

        return render(request, 'accueil.html', context)

    return render(request, 'accueil.html')