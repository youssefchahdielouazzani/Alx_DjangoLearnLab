from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# ---------------------------------------
# List all books (accessible par tous)
# ---------------------------------------
class BookListView(generics.ListAPIView):
    """
    GET /books/
    Retourne la liste complète des livres.
    Accessible par tous les utilisateurs.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # lecture publique, modification réservée aux authentifiés

# ---------------------------------------
# Retrieve a single book by ID
# ---------------------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<int:pk>/
    Retourne le détail d'un livre spécifique.
    Accessible par tous les utilisateurs.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# ---------------------------------------
# Create a new book (authentifié uniquement)
# ---------------------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Permet aux utilisateurs authentifiés de créer un nouveau livre.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

# ---------------------------------------
# Update an existing book (authentifié uniquement)
# ---------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/update/<int:pk>/
    Permet aux utilisateurs authentifiés de mettre à jour un livre existant.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# ---------------------------------------
# Delete a book (authentifié uniquement)
# ---------------------------------------
class DeleteView(generics.DestroyAPIView):
    """
    DELETE /books/delete/<int:pk>/
    Supprime un livre (authentifié uniquement)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
