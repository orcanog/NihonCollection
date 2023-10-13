from django.shortcuts import render
import requests

def get_anime_data(anime_id):
    url = f"https://kitsu.io/api/edge/anime/{anime_id}"
    headers = {
        "Accept": "application/vnd.api+json",
        "Content-Type": "application/vnd.api+json",
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]
    else:
        return None

def anime_detail(request, anime_id):
    anime_data = get_anime_data(anime_id)

    if anime_data is None:
        # Gère le cas où l'API ne renvoie pas de données pour l'ID d'anime donné
        context = {
            'error_message': "Anime non trouvé",
        }
    else:
        # Récupère les informations de l'anime à partir des données renvoyées par l'API
        anime_title = anime_data["attributes"]["titles"]["en_jp"] or anime_data["attributes"]["titles"]["ja_jp"]
        anime_image_url = anime_data["attributes"]["posterImage"]["large"]
        anime_description = anime_data["attributes"]["description"]

        context = {
            'anime_title': anime_title,
            'anime_image_url': anime_image_url,
            'anime_description': anime_description,
        }

    return render(request, 'detail.html', context)