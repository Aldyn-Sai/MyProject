from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, AddCommentToPostView, LikePostView

urlpatterns = [
    path('posts/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/comment/', AddCommentToPostView.as_view(), name='add_comment_to_post'),
    path('post/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
]
