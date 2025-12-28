from django.urls import path
from . import views
from .views import PostByTagListView

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),

    # ✅ OBLIGATOIRE POUR ALX
    path(
        'tags/<slug:tag_slug>/',
        PostByTagListView.as_view(),
        name='posts_by_tag'
    ),

    path('search/', views.search_posts, name='search'),
]



