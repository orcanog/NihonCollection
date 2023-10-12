from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from Collection.models import FavoriDb, AnimeInfos
import requests


class FavoriView(TemplateView):
    template_name = "favori.html"

@login_required
def ajouter_aux_favoris(request):
    if request.method == "POST" and request.user.is_authenticated:
        anime_id = request.POST.get("anime_id")      
        try:
            anime = AnimeInfos.objects.get(id_anime=anime_id)
        except AnimeInfos.DoesNotExist:
            return JsonResponse({"success": False, "error": "Anime not found"})
        user_pseudo = request.user.username  
        existe_deja = FavoriDb.objects.filter(id_anime_key=anime_id, pseudo=user_pseudo).exists()
        if not existe_deja:
            favoris = FavoriDb(id_anime_key=anime, pseudo=user_pseudo)
            favoris.save()
            return JsonResponse({"success": True , 'existe_deja' : existe_deja})
        else:
            return JsonResponse({"success": False, "error": "Anime already in favorites"})
    else:
        return JsonResponse({"success": False})
    
    
@login_required
def supprimer_des_favoris(request):
    if request.method == "POST" and request.user.is_authenticated:
        anime_id = request.POST.get("anime_id")
        user_pseudo = request.user.username

        # Recherchez l'élément dans les favoris de l'utilisateur
        try:
            favori = FavoriDb.objects.get(id_anime_key__id_anime=anime_id, pseudo=user_pseudo)
        except FavoriDb.DoesNotExist:
            return JsonResponse({"success": False, "error": "Favori not found"})

        # Supprimez l'élément des favoris de l'utilisateur
        favori.delete()

        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})


#verifier si un anime est deja dans les favori et si le user est connecte pour y acceder
def verifFav(request,anime_id):
        if request.user.is_authenticated:

            user_pseudo = request.user.username

            existe_deja = FavoriDb.objects.filter(id_anime_key=anime_id, pseudo=user_pseudo).exists()

            return existe_deja
        
        else :
            return False 

# fonction pour afficher les animes favoris dans la page html : MARCHE PAS ENCORE
# def favori(request):
#     user_favorites = FavoriDb.objects.filter(user=request.user)
#     return render(request, 'favori.html', {'user_favorites': user_favorites})

#    path('favori/', favorites.animeFavoris, name="favori"), j'ai changé l'url pour qu'il appelle cette method quand tu arrives sur la page fav

#La premiere method permets de retourner un json avec les une liste ID précis que va donner la deuxieme method
#La deuxieme method va chercher l'utilisateur connecté pour filtrer sur ses favoris et resortir les IDs a donner 
#a la première method pour ensuite boucler et tt mettre dans un dictionnaire que tu vas print comme pour la page d'accueil


def rechercheIdAnime(animeChercher):
    #Tu mets un /{} avec un f devant pour pouvoir lui passer une variable
    response = requests.get(f'https://kitsu.io/api/edge/anime/{animeChercher}')

    if response.status_code == 200:
        anime_data = response.json()
        #On recupère ici ce qu'on va utilisé en bas
        anime_info = {
            'title': anime_data['data']['attributes']['titles']['en_jp'],
            'img': anime_data['data']['attributes']['posterImage']['small'],
            'id': anime_data['data']['id'],
            'anime_type': anime_data['data']['type']
        }
        return anime_info
    else:
        print('La requête a échoué avec le code de statut :', response.status_code)
        return None


def animeFavoris(request):
    #Tu vas chercher le pseudo de l'user connecté
    if request.user.is_authenticated:
        user_pseudo = request.user.username
        #tu filtres sur son pseudo pour ressortir que les IDs d'anime qui lui sont attribué
        favoris = FavoriDb.objects.filter(pseudo=user_pseudo)
        #tu récup les id du user filtrer au dessus
        anime_ids = [favori.id_anime_key_id for favori in favoris]
        user_favorites = []
        #Tu vas chercher les donnés demandé en bas pour chaque ID
        for anime_id in anime_ids:
            anime = rechercheIdAnime(anime_id)
            if anime:
                title = anime['title'] 
                img = anime['img'] 
                existe_deja = True 
                anime_type = anime['anime_type'] 
                user_favorites.append((title, img, anime_id, existe_deja, anime_type))

        return render(request, 'favori.html', {'user_favorites': user_favorites})
    else:
        error_message = "Vous devez être connecté pour voir vos favoris."
        return render(request, 'favori.html', {'error_message': error_message})