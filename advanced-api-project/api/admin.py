from django.contrib import admin
from .models import Book

# Enregistrer le modèle Book pour l'administration Django
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_date', 'created_by')
    search_fields = ('title', 'author')

