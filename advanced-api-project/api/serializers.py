from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# ----------------------------------------------------------------------
# Serializer pour le modèle Book
# ----------------------------------------------------------------------
class BookSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Book.
    Permet de convertir les instances Book en JSON et vice versa.
    Inclut une validation personnalisée pour s'assurer que
    l'année de publication n'est pas dans le futur.
    """

    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Validation personnalisée : publication_year ne peut pas être dans le futur.
        """
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "L'année de publication ne peut pas être dans le futur."
            )
        return value

# ----------------------------------------------------------------------
# Serializer pour le modèle Author avec liste imbriquée de livres
# ----------------------------------------------------------------------
class AuthorSerializer(serializers.ModelSerializer):
    """
    Sérialiseur pour le modèle Author.
    Inclut le champ 'name' et une liste imbriquée 'books' qui utilise BookSerializer.
    La relation One-to-Many Author -> Book est gérée via related_name='books'.
    """

    books = BookSerializer(many=True, read_only=True)  # nested serializer

    class Meta:
        model = Author
        fields = ['name', 'books']
