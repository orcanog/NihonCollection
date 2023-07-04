### ESIEE-IT - BTS SIO SLAM 2023 - AP n°3 Collector
#### NOM PROJET : Kitsu.io
#### OG Orcan, IMZILEN Abdelali, BONAMI Nirmala
#### version 1.0 le 26/04/2023

### DESCRIPTION
Une application mobile sur la recherche de personnage d'anime à l'aide de l'API Kitsu.io

Objectif : Proposer aux utilisateurs, sur mobile et ordinateur, la possibilté de créer une collection de leurs personnages favoris provenant de séries d'animation japonaise.

### FONCTIONNALITES
* Permettre à chaque utilisateur de mettre en favoris leurs personnages préférés impliquant donc la création d'une collection de favoris.
* Proposer aux visiteurs tous les personnages contenus dans l'API Kitsu.io et leur permettre d'utiliser le formulaire de recherche.
* Le formulaire de recherche permettra au visiteur de rechercher un personnage à partir de son nom ou de critères cohérents d'un anime ou manga dont le type de série, la date de sortie d'un anime ou manga afin d'afficher les personnages correspondant aux critères choisis.
* Sur la page d'accueil du site web, proposer la création d'un compte utilisateur à un visiteur, afin ensuite de pouvoir gérer une collection de personnages.
* Chaque élément des résultats de la recherche doit pouvoir être mis en favoris par l'utilisateur, ce qui aura pour effet d'insérer toutes les données de l'élément mit en favori dans la base de données.
* Chaque utilisateur aura une page personnelle permettant de voir ses éléments mis en favoris.
* Proposer une page d'administration pour les admins authentifiés leur permettant de pouvoir gérer les utilisateurs.


### Spécifications techniques
Langages utilisés : 
- Front-end : HTML/CSS/JS
- Back-end : Django (Python)

Langages choisis et utilisés dans le cadre d'un projet scolaire pour découvrir un nouveau framework.

### Sécurité
- Mot de passe pour les utilisateurs : 16 caractères minimums dont 1 majuscule, 1 minuscule, 1 chiffre et 2 caractères spéciaux
- Mot de passe pour les administrateurs : 18 caractères minimums dont 1 majuscule, 1 minuscule, 2 chiffre et 3 caractères spéciaux
- Cryptage de mot de passe afin d'éviter le stockage en clair dans la base de données.

### Estimation budgétaire
- Achat du nom de domaine

### Clauses contractuelles
- Respect RGPD