from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .fields import UpperCaseCharField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, blank=True)
    highest_qualification = models.CharField(max_length=50, blank=True)
    qualification_stream = models.CharField(max_length=50, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    reading_frequency = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    uid = models.CharField(max_length=128, unique=True)
    title = models.CharField(max_length=256)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    

    def __str__(self):
        return self.title 