from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404
from users import views as user_views
from .views import (
    CommunityListView,
    CommunityDetailView,
    CommunityCreateView,
    CommunityUpdateView,
    CommunityDeleteView,
    subscribe,
    unsubscribe,
    post_create,
    PostDetailView,
    PostDeleteView,
    PostUpdateView,
    create_comment,
)

urlpatterns = [
    ## Communities urls
    path('', CommunityListView.as_view(), name='communities-home'),
    path('community/new/', CommunityCreateView.as_view(), name='community-create'),
    path('community/<int:pk>', CommunityDetailView.as_view(), name='community-detail'),
    path('community/<int:pk>/update/', CommunityUpdateView.as_view(), name='community-update'),
    path('community/<int:pk>/delete/', CommunityDeleteView.as_view(), name='community-delete'),
    path('community/<int:community_id>/subscribe/', subscribe, name='community-subscribe'),
    path('community/<int:community_id>/unsubscribe/', unsubscribe, name='community-unsubscribe'),
    ## Posts urls
    path('community/<int:community_id>/post/new/', post_create, name='post-create'),
    path('post/<int:pk>', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/comment/new/', create_comment, name='create-comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
