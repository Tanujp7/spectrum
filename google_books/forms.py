from django import forms

from items.models import Book, BookProfile

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('volume_id', 'title')

class BookProfileForm(forms.ModelForm):
    class Meta:
        model = BookProfile
        fields = (  'isbn',
                    'description',
                    'publication_date',
                    'cover_image_link',
                    'page_count',
                    'rating',
                    'rating_count',
                    'language',
                    'cost',
                    'tags',
                    'author',
                    'publisher')
