from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomAuthenticationForm

class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'login.html'
