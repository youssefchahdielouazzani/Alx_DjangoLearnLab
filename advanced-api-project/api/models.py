from django.db import models

# Author model: représente un auteur (un auteur peut avoir plusieurs livres).
class Author(models.Model):
    name = models.CharField(max_length=100)  # Nom complet de l'auteur

    def __str__(self):
        return self.name


# Book model: représente un livre lié à un auteur.
# Relation One-to-Many : un Author peut avoir plusieurs Books.
class Book(models.Model):
    title = models.CharField(max_length=200)  # Titre du livre
    publication_year = models.IntegerField()  # Année de publication
    author = models.ForeignKey(
        Author,
        related_name='books',      # Permet : author.books.all()
        on_delete=models.CASCADE   # Supprime les livres si l'auteur est supprimé
    )

    def __str__(self):
        return self.title
