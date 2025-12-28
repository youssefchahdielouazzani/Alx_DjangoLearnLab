from .models import Author, Book, Library, Librarian

# All books by a specific author
author = Author.objects.first()
books_by_author = Book.objects.filter(author=author)

# All books in a library
library = Library.objects.first()
books_in_library = library.books.all()

# Librarian for a library
librarian = Librarian.objects.get(library=library)

