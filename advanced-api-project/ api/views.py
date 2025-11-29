from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer

# ------------------------------------------
# BookListView : liste des livres avec
# filtrage, recherche et tri (ordering)
# ------------------------------------------
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Backends pour filtrage, recherche et ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Champs sur lesquels on peut filtrer
    filterset_fields = ['title', 'author', 'publication_year']

    # Champs sur lesquels on peut faire une recherche textuelle
    search_fields = ['title', 'author']

    # Champs sur lesquels on peut trier
    ordering_fields = ['title', 'publication_year']

    # Tri par défaut
    ordering = ['title']
