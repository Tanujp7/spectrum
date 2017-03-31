from django import forms

from .models import BookRating, RatingLog

class BookRatingForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('rating')

class RatingLogForm(forms.ModelForm):
    class Meta:
        model = BookProfile
        fields = ('rating')
