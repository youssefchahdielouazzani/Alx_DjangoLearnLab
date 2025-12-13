from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # 1. Tous les livres d'un auteur spécifique
    try:
        author = Author.objects.get(name='Nom de l\'auteur')
        books_by_author = author.books.all()
        print(f"Books by {author.name}: {[book.title for book in books_by_author]}")
    except Author.DoesNotExist:
        print("Auteur non trouvé.")

    # 2. Tous les livres dans une bibliothèque
    try:
        library = Library.objects.get(name='Nom de la bibliothèque')
        books_in_library = library.books.all()
        print(f"Books in {library.name}: {[book.title for book in books_in_library]}")
    except Library.DoesNotExist:
        print("Bibliothèque non trouvée.")

    # 3. Le bibliothécaire d'une bibliothèque
    try:
        librarian = library.librarian
        print(f"Librarian of {library.name}: {librarian.name}")
    except Librarian.DoesNotExist:
        print("Bibliothécaire non trouvé pour cette bibliothèque.")

# Si ce script est exécuté directement
if __name__ == '__main__':
    import django
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
    django.setup()
    run_queries()

