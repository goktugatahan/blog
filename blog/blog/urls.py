from django.contrib import admin
from django.urls import path, include
from users import urls as user_urls
from posts import urls as posts_urls
from dashboard import urls as dashboard_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/users/", include(user_urls)),
    path("api/posts/", include(posts_urls)),
    path('dashboard/', include(dashboard_urls)),
]
