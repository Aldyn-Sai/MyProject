from django.contrib import admin
from django.urls import path
from blog.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, AddCommentToPostView, LikePostView, login_view, add_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),  # Убедитесь, что этот маршрут существует
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/comment/', AddCommentToPostView.as_view(), name='add_comment_to_post'),
    path('post/<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('login/', login_view, name='login'),
    path('add_item/', add_item, name='add_item'),
]
