from django.urls import path
from .views import VoteCreateView

app_name = "votes"

urlpatterns = [
    path('<uuid:board_id>/<uuid:post_id>/vote_new', VoteCreateView.as_view(), name='vote_new')
]