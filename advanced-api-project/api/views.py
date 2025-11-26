from rest_framework import generics
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


# Liste + création de livres
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Liste + création d'auteurs (avec affichage des livres imbriqués)
class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

