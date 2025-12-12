# CRUD Operations Summary

## 1. CREATE
>>> from bookshelf.models import Book
>>> book = Book.objects.create(
...     title="1984",
...     author="George Orwell",
...     publication_year=1949
... )
# <Book: 1984>

---

## 2. RETRIEVE
>>> from bookshelf.models import Book
>>> book = Book.objects.first()
>>> book
# <Book: 1984>
>>> book.title
# '1984'
>>> book.author
# 'George Orwell'
>>> book.publication_year
# 1949

---

## 3. UPDATE
>>> from bookshelf.models import Book
>>> book = Book.objects.first()
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book.title
# 'Nineteen Eighty-Four'

---

## 4. DELETE
>>> from bookshelf.models import Book
>>> book = Book.objects.first()
>>> book.delete()
# (1, {'bookshelf.Book': 1})

>>> Book.objects.all()
# <QuerySet []>

