const profileMenu = document.getElementById('profileMenu');
const profile = document.getElementById('profile');

profile.addEventListener('click', function(event) {
    event.stopPropagation();
    profileMenu.classList.toggle('show');
});

document.addEventListener('click', function() {
    profileMenu.classList.remove('show');
});


const searchContainer = document.querySelector('.search-container');
const searchIcon = document.getElementById('search-git icon');
const searchInput = document.getElementById('search-input');

searchIcon.addEventListener('click', () => {
    searchContainer.classList.toggle('active');
    searchInput.focus();
});
