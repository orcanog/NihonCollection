function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Chercher le cookie avec le nom csrftoken
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener("DOMContentLoaded", function () {
    var favorisButtons = document.querySelectorAll(".favoris-button");
    var removeFavorisButtons = document.querySelectorAll(".remove-favoris-button");

    favorisButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var animeId = this.getAttribute("data-anime-id");

            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/ajouter_aux_favoris/", true);
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));

            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200) {
                        var response = JSON.parse(xhr.responseText);
                        if (response.success) {
                            console.log("Anime ajouté aux favoris !");
                            // Mettez à jour l'interface utilisateur si nécessaire
                        } else {
                            console.log("Une erreur s'est produite lors de l'ajout aux favoris.");
                        }
                    } else {
                        console.log("Une erreur s'est produite lors de la requête AJAX.");
                    }
                }
            };

            xhr.send("anime_id=" + animeId);
        });
    });

    removeFavorisButtons.forEach(function (button) {
        button.addEventListener("click", function () {
            var animeId = this.getAttribute("data-anime-id");

            var xhr = new XMLHttpRequest();
            xhr.open("POST", "/supprimer_des_favoris/", true);
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));

            xhr.onreadystatechange = function () {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200) {
                        var response = JSON.parse(xhr.responseText);
                        if (response.success) {
                            console.log("Anime supprimé des favoris !");
                            // Mettez à jour l'interface utilisateur si nécessaire
                        } else {
                            console.log("Une erreur s'est produite lors de la suppression des favoris.");
                        }
                    } else {
                        console.log("Une erreur s'est produite lors de la requête AJAX.");
                    }
                }
            };

            xhr.send("anime_id=" + animeId);
        });
    });
});
