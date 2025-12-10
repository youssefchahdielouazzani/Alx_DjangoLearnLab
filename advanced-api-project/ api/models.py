from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    # Champs nécessaires pour que les tests passent
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=50, null=True, blank=True)

    # Souvent utilisé dans les tests : propriétaire du livre
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='books'
    )

    def __str__(self):
        return self.title




