from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)           # Titre du livre
    author = models.CharField(max_length=100)          # Nom de l'auteur
    published_date = models.DateField(null=True, blank=True)  # Date de publication
    isbn = models.CharField(max_length=13, unique=True)       # ISBN
    pages = models.PositiveIntegerField(null=True, blank=True)  # Nombre de pages
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)  # Couverture
    language = models.CharField(max_length=20, default='English')  # Langue

    def __str__(self):
        return f"{self.title} by {self.author}"

