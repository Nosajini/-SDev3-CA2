from os import name, stat
from django.urls import path
from .views import loginPageView, signupPageView, UserEditView, ProfilePageView


urlpatterns = [
    path('', loginPageView.as_view(), name="login"),
    path('signup/', signupPageView.as_view(), name="signup"),
    path('<int:pk>/edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name='show_profile'),
]