from django.db.models import fields
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from .models import Profile

# Create your views here.
class loginPageView(TemplateView):
    template_name = 'registration/login.html'

class signupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserEditView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['body', 'image']
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user.profile

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'
