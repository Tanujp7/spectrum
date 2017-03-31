from django import forms

from items.models import Book, BookProfile

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('volume_id', 'title')
