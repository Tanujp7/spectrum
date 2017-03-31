from django import forms

from .models import BookRating, RatingLog

class BookRatingForm(forms.ModelForm):
    class Meta:
        model = BookRating
        fields = ('rating')

class RatingLogForm(forms.ModelForm):
    class Meta:
        model = RatingLog
        fields = ('rating')
