from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from taggit.managers import TaggableManager

from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator

from .fields import UpperCaseCharField


class Location(models.Model):
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    CONTINENTS = (
        ('Africa', 'Africa'),
        ('Antarctica', 'Antarctica'),
        ('Asia', 'Asia'),
        ('Australia', 'Australia'),
        ('Europe', 'Europe'),
        ('North America', 'North America'),
        ('South America', 'South America')
    )
    continent = models.CharField(max_length=15, choices=CONTINENTS,null=False)

    def __str__(self):
        return (self.city + ', ' + self.state + ', ' + self.country + ', ' + self.continent)


class BookUID(models.Model):
    BOOK_UID_TYPES = (
        ('ISBN10', 'ISBN10'),
        ('ISBN13', 'ISBN13'),
        ('ASIN', 'Amazon UID')
    )
    uid_type = models.CharField(max_length=10, choices=BOOK_UID_TYPES)
    uid = models.CharField(max_length=64, unique=True)
    
    class Meta:
        verbose_name = 'Book UID'
    
    def __str__(self):
        return (self.uid_type + ' ' + self.uid)
    
class Qualification(models.Model):
    qualification_name = models.CharField(max_length=60, null=True)
    qualification_stream = models.CharField(max_length=60, null=True)

    def __str__(self):
        return (self.qualification_name + ' ' + self.qualification_stream)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    birth_date = models.DateField(null=True, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES)
    highest_qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, null=True)
    occupation = models.CharField(max_length=100, blank=True)
    ALMOST_NEVER = 5
    SOMETIMES = 15
    FEW_TIMES_A_MONTH = 50
    FEW_TIMES_A_WEEK = 150
    ALMOST_EVERYDAY = 300
    READING_FREQUENCY_CHOICES = (
        (ALMOST_NEVER, 'Almost Never (0-5 times a year)'),
        (SOMETIMES, 'Sometimes (6-15 times a year)'),
        (FEW_TIMES_A_MONTH, 'Few times a month (Once a week)'),
        (FEW_TIMES_A_WEEK, 'Few times a week (2-4 times a week)'),
        (ALMOST_EVERYDAY, 'Almost Everyday (6 times a week)')
    )
    reading_frequency = models.CharField(max_length=50, choices=READING_FREQUENCY_CHOICES)

    def __str__(self):
        return self.user
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.full_name

class Book(models.Model):
    uid = models.ManyToManyField(BookUID, verbose_name = 'Book UID')
    title = models.CharField(max_length=256)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_year = models.SmallIntegerField(validators=[MinValueValidator(1600), MaxValueValidator(2100)])

    def __str__(self):
        return self.title 

class BookProfile(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    tags = TaggableManager()
    description = models.CharField(max_length=1024)
    
    class Meta:
        verbose_name = 'Book Profile'
        
    def __str__(self):
        return self.book.title
    
class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(choices=[(i, i) for i in range(1, 6)], default=1)
    
    class Meta:
        unique_together = ('user', 'book')
        verbose_name = 'Book Rating'
    
    def __str__(self):
        return (str(self.rating) + '* - ' + str(self.book.title) + ' - rated by - ' + str(self.user))

class BookLikeDislike(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.SmallIntegerField(choices=[(i, i) for i in range(-1, 2)], default=0)
    
    class Meta:
        unique_together = ('user', 'book')
        verbose_name = 'Book Like/Dislike'
        verbose_name_plural = 'Book Likes/Dislikes'
    
    def __str__(self):
        return (str(self.like) + '* - ' + str(self.book.title) + ' - by - ' + str(self.user))
    
class BookInterestLog(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest_score = models.SmallIntegerField(default=0)
    
    class Meta:
        verbose_name = 'Book Interest Log'
    
    def __str__(self):
        return (str(self.interest_score) + '* - ' + str(self.book.title) + ' - by - ' + str(self.user))
    
class AuthorLikeDislike(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.SmallIntegerField(choices=[(i, i) for i in range(-1, 2)], default=0)
    
    class Meta:
        unique_together = ('user', 'author')
        verbose_name = 'Author Like/Dislike'
        verbose_name_plural = 'Author Likes/Dislikes'
    
    def __str__(self):
        return (str(self.like) + '* - ' + str(self.author.full_name) + ' - by - ' + str(self.user))