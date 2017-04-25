from django.contrib import admin
from .models import Book, BookProfile, Entity

# Register your models here.
admin.site.register(Book)
admin.site.register(Entity)
admin.site.register(BookProfile)
