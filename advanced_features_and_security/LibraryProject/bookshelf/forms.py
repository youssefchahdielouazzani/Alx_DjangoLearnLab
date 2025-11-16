from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        return forms.utils.strip_tags(title)

    def clean_author(self):
        author = self.cleaned_data.get('author')
        return forms.utils.strip_tags(author)

