from django.contrib import admin

from .models import BookRating, BookLikeDislike, BookInterestLog

# Register your models here.

admin.site.register(BookRating)
admin.site.register(RatingLog)
