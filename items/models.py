from django.db import models

from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

from taggit.managers import TaggableManager

class Book(models.Model):
    volume_id = models.CharField(max_length=25, unique=True)
    title = models.CharField(max_length=256, null=True, default='unknown')

    def __str__(self):
        return self.title

class Key(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True, default=None)
    stop_bighuge = models.NullBooleanField(blank=True, default=False)
    stop_wordsapi = models.NullBooleanField(blank=True, default=False)

    def __str__(self):
        return (str(self.name))

class BookProfile(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=50, null=True, blank=True, default='')
    description = models.CharField(max_length=5000, null=True, blank=True, default='')
    publisher = models.CharField(max_length=256, null=True, blank=True, default='unknown')
    author = models.CharField(max_length=256, null=True, blank=True, default='unknown')
    publication_date = models.DateField(null=True, blank=True)
    cover_image_link = models.CharField(max_length=360, null=True, blank=True, default='https://upload.wikimedia.org/wikipedia/commons/a/ac/No_image_available.svg')
    page_count = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], null=True, blank=True, default=0.0)
    rating_count = models.PositiveIntegerField(null=True, blank=True, default=0)
    language = models.CharField(max_length=4, null=True, blank=True, default='en')
    cost = models.CharField(max_length=20, null=True, blank=True, default='0')
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Book Profile'

    def __str__(self):
        return self.book.title
