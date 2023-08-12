from django.urls import path, include
from .views import PostsList

urlpatterns = [
    path('', PostsList.as_view() ),
]