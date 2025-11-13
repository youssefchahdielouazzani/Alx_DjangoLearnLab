from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


# -------------------------------
# 1️⃣ Function-based view : Liste de tous les livres
# -------------------------------
def list_books(request):
    """
    Affiche la liste de tous les livres enregistrés dans la base de données.
    """
    books = Book.objects.all()  # Récupère tous les livres
    context = {'books': books}
    return render(request, 'list_books.html', context)


# -------------------------------
# 2️⃣ Class-based view : Détails d'une bibliothèque
# -------------------------------
class LibraryDetailView(DetailView):
    """
    Affiche les détails d'une bibliothèque spécifique, y compris les livres disponibles.
    """
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'


