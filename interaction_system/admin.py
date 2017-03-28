from django.contrib import admin

from .models import Location, Book, BookRating, BookLikeDislike, BookProfile, BookInterestLog

# Register your models here.

admin.site.register(Book)
admin.site.register(BookRating)
admin.site.register(BookProfile)
admin.site.register(BookInterestLog)
admin.site.register(BookLikeDislike)
admin.site.register(Location)
