from django.contrib import admin

from .models import Location, Publisher, Author, Book, BookUID, BookRating

# Register your models here.

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookUID)
admin.site.register(BookRating)
admin.site.register(Location)