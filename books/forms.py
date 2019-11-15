from django import forms
from .models import Publisher, Author, Book

class AddBook(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('author', 'publisher', 'name', 'year', 'genre', 'description', 'image')