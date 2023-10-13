const searchContainer = document.querySelector('.search-container');
const searchIcon = document.getElementById('search-git icon');
const searchInput = document.getElementById('search-input');
const searchBar = document.querySelector('#search-form');
const animeAPI = document.querySelector(".image-container");
const animeResult = document.querySelector(".result-container");
let timerId;

profile.addEventListener('click', function(event) {
    event.stopPropagation();
    profileMenu.classList.toggle('show');
});

document.addEventListener('click', function() {
    profileMenu.classList.remove('show');
});

/**searchIcon.addEventListener('click', () => {
    searchContainer.classList.toggle('active');
    searchInput.focus();
});**/

//Fonction déclenchée à chaque saisie dans la barre de recherche
searchBar.addEventListener("input", (event) => {
    // Récupération de la valeur saisie dans la barre de recherche
    const query = event.target.value; 
  
    // Si le champ est vide, on cache les résultats de recherche
    if (query === "") { 
      animeResult.classList.add("hidden");
      animeAPI.classList.remove("hidden");
      return;
    }

    // On clear le timeout précédent
    clearTimeout(timerId); 

    // On définit un timeout de 500 millisecondes avant de déclencher l'appel API
    timerId = setTimeout(() => { 
        // On appelle l'API Kitsu pour récupérer les résultats de recherche
      fetch(`https://kitsu.io/api/edge/anime?filter[text]=${query}`) 
       // On convertit la réponse en JSON
        .then((response) => response.json())
         // On traite les données récupérées
        .then((data) => {
            // On vide les résultats de recherche précédents
          animeResult.innerHTML = ""; 
  
          // Pour chaque résultat de recherche, on crée un élément HTML pour l'afficher
          data.data.forEach((item) => { 
            const animeContainer = document.createElement("div");
            animeContainer.classList.add("anime-container");
  
            const animeTitle = document.createElement("h3");
            animeTitle.classList.add("anime-title");
            animeTitle.textContent = item.attributes.titles.en_jp || item.attributes.titles.ja_jp || "No title";
  
            const animeImage = document.createElement("img");
            animeImage.classList.add("anime-image");
            animeImage.src = item.attributes.posterImage.small;
            animeImage.alt = "Image";
  
            animeContainer.appendChild(animeTitle);
            animeContainer.appendChild(animeImage);
            animeResult.appendChild(animeContainer);
          });
  
          // On affiche la recherche
          animeResult.classList.remove("hidden");
          // On cache les animes du catalogue 
          animeAPI.classList.add("hidden"); 
        })
        // En cas d'erreur, on affiche l'erreur dans la console
        .catch((error) => {
            console.error(error);
        });
    }, 500);
});