# api/views.py

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from books.models import Book
from books.serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    API view pour lister les livres avec :
    - filtrage par title, author, publication_year
    - recherche textuelle sur title et author
    - tri (ordering) sur title et publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Backends pour filtrage, recherche et tri
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Champs pour le filtrage exact
    filterset_fields = ['title', 'author', 'publication_year']

    # Champs pour la recherche textuelle
    search_fields = ['title', 'author']

    # Champs pour le tri
    ordering_fields = ['title', 'publication_year']

    # Tri par défaut
    ordering = ['title']
