const profileMenu = document.getElementById('profileMenu');
const profile = document.getElementById('profile');

profile.addEventListener('click', function(event) {
    event.stopPropagation();
    profileMenu.classList.toggle('show');
});

document.addEventListener('click', function() {
    profileMenu.classList.remove('show');
});
