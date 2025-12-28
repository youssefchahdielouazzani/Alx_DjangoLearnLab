from django.shortcuts import render
from .models import Library, Book, Author, Librarian

# Exemple de vue simple affichant toutes les bibliothèques et leurs livres
def library_list(request):
    libraries = Library.objects.all()
    context = {'libraries': libraries}
    return render(request, 'relationship_app/library_list.html', context)

