from django.contrib import admin

from .models import Location, Publisher, Author, Book, BookUID, BookRating, BookLikeDislike, AuthorLikeDislike, BookProfile, BookInterestLog

# Register your models here.

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookUID)
admin.site.register(BookRating)
admin.site.register(BookProfile)
admin.site.register(BookInterestLog)
admin.site.register(BookLikeDislike)
admin.site.register(AuthorLikeDislike)
admin.site.register(Location)