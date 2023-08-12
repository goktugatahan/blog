from django.urls import path, include
from .views import PostsAPIView, PostAPIView

urlpatterns = [
    path('', PostsAPIView.as_view(),name="blog_get_posts"),
    path('post/<int:pk>/', PostAPIView.as_view(),name="blog_get_post"),
    path('post/delete/', PostAPIView.as_view(),name="blog_delete_post"),
]