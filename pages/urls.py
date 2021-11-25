from django.urls import path
from .views import homePageView
from posts.views import PostListHome

urlpatterns = [
    path('', PostListHome.as_view(), name='home'),
]

