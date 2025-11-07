from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Enregistrer les modèles pour l'admin
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
