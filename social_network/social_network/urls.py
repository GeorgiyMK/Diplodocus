from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet, CommentViewSet, LikeViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'likes', LikeViewSet, basename='like')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token),  # получение токена авторизации
]
