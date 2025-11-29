from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# -------------------------------
# List all Books (GET)
# -------------------------------
class BookListView(generics.ListAPIView):
    """
    Returns a list of all books.
    Accessible to everyone (AllowAny).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -------------------------------
# Retrieve a Single Book (GET)
# -------------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    Returns a single book by ID.
    Accessible to everyone (AllowAny).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# -------------------------------
# Create a Book (POST)
# -------------------------------
class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    Only authenticated users can create.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Hook used by ALX requirements to customize behavior if needed
        serializer.save()


# -------------------------------
# Update a Book (PUT / PATCH)
# -------------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Only authenticated users can update.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        # Custom update behavior
        serializer.save()


# -------------------------------
# Delete a Book (DELETE)
# -------------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book.
    Only authenticated users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

