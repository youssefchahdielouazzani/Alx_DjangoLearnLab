# relationship_app/views.py

from django.http import HttpResponse
from .models import Book

def list_books(request):
    """
    Vue fonctionnelle qui renvoie une simple liste texte de livres
    sous la forme : "Titre - NomAuteur"
    """
    books = Book.objects.all()

    # Construire la sortie en tenant compte de variantes du modèle Author
    lines = []
    for book in books:
        # Cas 1 : author a un champ 'name'
        if hasattr(book.author, "name"):
            author_display = book.author.name
        # Cas 2 : author a 'first_name' et 'last_name'
        elif hasattr(book.author, "first_name") and hasattr(book.author, "last_name"):
            author_display = f"{book.author.first_name} {book.author.last_name}"
        # Cas 3 : fallback (si author est une simple chaine ou autre)
        else:
            author_display = str(book.author)

        lines.append(f"{book.title} - {author_display}")

    # Joindre avec des <br> pour l'affichage HTML simple
    output = "<br>".join(lines) if lines else "Aucun livre trouvé."
    return HttpResponse(output)

