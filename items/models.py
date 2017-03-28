from django.db import models

from taggit.managers import TaggableManager

from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator


class Book(models.Model):
    uid = models.CharField(max_length=256)
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title

class BookProfile(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    authors = models.CharField(max_length=1024)
    publisher = models.CharField(max_length=256)
    publication_year = models.SmallIntegerField(validators=[MinValueValidator(1600), MaxValueValidator(2100)])
    thumbnail = models.CharField(max_length=1024)
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Book Profile'

    def __str__(self):
        return self.book.title
