from django.urls import path
from .views import PostDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns = [
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

    # Création d'un commentaire
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),

    # Modification d'un commentaire
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),

    # Suppression d'un commentaire
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]


