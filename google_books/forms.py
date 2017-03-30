from django import forms

from items.models import Book, BookProfile

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ()


class AddBookProfileForm(forms.ModelForm):
    class Meta:
        model = BookProfile
        exclude = ()
