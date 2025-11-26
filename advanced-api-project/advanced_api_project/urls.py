from django.urls import path
from .views import AuthorListCreateView, BookListCreateView

urlpatterns = [
    # Liste et création des auteurs
    path('authors/', AuthorListCreateView.as_view(), name='authors-list-create'),
    
    # Liste et création des livres
    path('books/', BookListCreateView.as_view(), name='books-list-create'),
]

