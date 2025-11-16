from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        # Exemple simple de nettoyage : retirer les balises HTML pour éviter XSS
        return forms.utils.strip_tags(title)

    def clean_author(self):
        author = self.cleaned_data.get('author')
        return forms.utils.strip_tags(author)
