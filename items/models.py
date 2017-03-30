from django.db import models

from taggit.managers import TaggableManager

from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    volume_id = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    authors = models.ManyToManyField(Author)
    publishers = models.ManyToManyField(Publisher)

    def __str__(self):
        return self.title

class BookProfile(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
    publication_year = models.SmallIntegerField(validators=[MinValueValidator(1600), MaxValueValidator(2100)])
    thumbnail = models.CharField(max_length=1024)
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Book Profile'

    def __str__(self):
        return self.book.title
