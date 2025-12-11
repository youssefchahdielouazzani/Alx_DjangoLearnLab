from rest_framework import generics, permissions
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
    permission_classes = [permissions.AllowAny]  # lecture publique

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
    permission_classes = [permissions.AllowAny]

# ---------------------------------------
# Create a new book (authentifié uniquement)
# ---------------------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Permet aux utilisateurs authentifiés de créer un nouveau livre.
    Valide automatiquement les données via le serializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Optionnel : personnaliser la création si nécessaire.
        Par exemple, associer un utilisateur créateur :
        serializer.save(created_by=self.request.user)
        """
        serializer.save()

# ---------------------------------------
# Update an existing book (authentifié uniquement)
# ---------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/<int:pk>/update/
    Permet aux utilisateurs authentifiés de mettre à jour un livre existant.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# -----------------------------------

