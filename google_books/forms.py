from django import forms

from items.models import Book, BookProfile

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book

class AddBookProfileForm(forms.ModelForm):
    class Meta:
        model = BookProfile
