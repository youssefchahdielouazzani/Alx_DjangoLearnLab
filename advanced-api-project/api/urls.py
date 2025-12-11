from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    DeleteView,
)

urlpatterns = [
    # Liste de tous les livres
    path('books/', BookListView.as_view(), name='book-list'),

    # Détail d'un livre
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Créer un livre
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Mettre à jour un livre
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),

    # Supprimer un livre
    path('books/<int:pk>/delete/', DeleteView.as_view(), name='book-delete'),
]



