import requests
from django.shortcuts import render
from Collection.models import AnimeInfos
from Views.favorites import verifFav

def extract_info_anime(json_data, request):
    extracted_data = []
    if 'data' in json_data and len(json_data['data']) > 0:
        for anime_data in json_data['data']:
            title = anime_data['attributes']['titles']['en_jp'] or anime_data['attributes']['titles']['ja_jp']
            anime_type = anime_data['type']
            id = anime_data['id']
            img = anime_data['attributes']['posterImage']['small']
            existe_deja = verifFav(request, id)

            extracted_data.append({
                'title': title,
                'type': anime_type,
                'id': id,
                'img': img,
                'existe_deja': existe_deja
            })

            animeDb = AnimeInfos(id_anime=id,titre=title,image=img).save()

    return extracted_data



def MyView(request):
    api_url = "https://kitsu.io/api/edge/anime?page[limit]=20&page[offset]=0"

    response = requests.get(api_url)

    if response.status_code == 200:
        json_data = response.json()
        extracted_data = extract_info_anime(json_data, request)
        #print(extracted_data)
        context = {
            'extracted_data': extracted_data
        }
        return render(request, 'accueil.html', context)
    else:
        error_message = "Une erreur s'est produite lors de la requête. Code d'erreur : " + str(response.status_code)
        return render(request, 'error.html', {'error_message': error_message})
