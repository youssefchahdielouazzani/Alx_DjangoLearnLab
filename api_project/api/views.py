from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Vue DRF pour lister les livres et créer un livre
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

