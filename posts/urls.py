from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView,
                    PostList,
                    CommentCreateView)

app_name = 'posts'

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<uuid:board_id>/', PostList.as_view(), name = 'posts_by_board'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<uuid:board_id>/<uuid:post_id>/', PostDetailView.as_view(), name='post_detail'),
    path('<uuid:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<uuid:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<uuid:board_id>/<uuid:post_id>/comment_new', CommentCreateView.as_view(), name='comment_new')
]
