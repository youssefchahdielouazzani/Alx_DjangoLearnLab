from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


# BookSerializer: convertit le modèle Book <-> JSON
class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = '__all__'

    # Validation personnalisée:
    # L'année de publication ne peut pas dépasser l'année actuelle
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "L'année de publication ne peut pas être dans le futur."
            )
        return value


# AuthorSerializer: inclut une liste imbriquée de livres (nested serializer)
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
