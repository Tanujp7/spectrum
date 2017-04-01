from django import forms

from .models import BookRating

class BookRatingForm(forms.ModelForm):
    class Meta:
        model = BookRating
        fields = ('rating',)
