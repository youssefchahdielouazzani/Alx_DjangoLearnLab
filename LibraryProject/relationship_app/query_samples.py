from .models import Author, Book, Library, Librarian

def run_queries():
    # 1. Tous les livres d'un auteur spécifique
    author_name = "J.K. Rowling"
    try:
        author = Author.objects.get(name=author_name)
        print(f"Livres de {author_name}: {[book.title for book in author.books.all()]}")
    except Author.DoesNotExist:
        print(f"Aucun auteur trouvé avec le nom {author_name}")

    # 2. Liste de tous les livres dans une bibliothèque
    library_name = "Central Library"
    try:
        library = Library.objects.get(name=library_name)
        print(f"Livres dans {library_name}: {[book.title for book in library.books.all()]}")
    except Library.DoesNotExist:
        print(f"Aucune bibliothèque trouvée avec le nom {library_name}")

    # 3. Récupérer le bibliothécaire d'une bibliothèque
    try:
        librarian = library.librarian
        print(f"Le bibliothécaire de {library_name} est {librarian.name}")
    except Librarian.DoesNotExist:
        print(f"Aucun bibliothécaire assigné à {library_name}")

