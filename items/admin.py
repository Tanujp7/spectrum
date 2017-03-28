from django.contrib import admin
from .models import Book, BookProfile

# Register your models here.

admin.site.register(Book)
admin.site.register(BookProfile)
