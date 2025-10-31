from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # colonnes visibles
    list_filter = ('author', 'publication_year')           # filtres
    search_fields = ('title', 'author')                    # barre de recherche
