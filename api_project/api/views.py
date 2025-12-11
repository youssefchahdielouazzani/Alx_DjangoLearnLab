from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .permissions import IsOwner

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # protège toutes les actions

    # Si tu veux appliquer la permission "IsOwner" pour modification/suppression :
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwner()]
        return [IsAuthenticated()]




