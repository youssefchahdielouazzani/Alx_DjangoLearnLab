# Delete the book and verify deletion

>>> from bookshelf.models import Book
>>> book = Book.objects.first()
>>> book.delete()
# (1, {'bookshelf.Book': 1})

# Confirm deletion
>>> Book.objects.all()
# <QuerySet []>

