# importer depuis le module auth la class UserCreationForm qui facilite la creation de formulaire
from django.contrib.auth.forms import UserCreationForm
# faciliter la redirection des utilisateurs vers un autre URL
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    # la class UserCreationForm n'a pas de vue par defaut donc il faut lui en specifier une, ici signup.html
    template_name = "registration/signup.html"