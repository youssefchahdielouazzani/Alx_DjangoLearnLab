from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ============================
# LIST & DETAIL (lecture seule)
# ============================

class BookListView(generics.ListAPIView):
    """
    GET /books/
    Retourne la liste de tous les livres.
    Accessible à tous (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<id>/
    Retourne le détail d'un livre par son ID.
    Accessible à tous (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# ============================
# CREATE / UPDATE / DELETE
# ============================

class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Crée un nouveau livre.
    Accessible uniquement aux utilisateurs authentifiés.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/<id>/update/
    Modifie un livre existant.
    Accessible uniquement aux utilisateurs authentifiés.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/<id>/delete/
    Supprime un livre existant.
    Accessible uniquement aux utilisateurs authentifiés.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
