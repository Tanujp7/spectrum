from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinValueValidator

class Career(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='1')
    qualification_name = models.CharField(max_length=60, blank=True, default='')
    qualification_stream = models.CharField(max_length=60, blank=True, default='')
    occupation = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return (str(self.qualification_stream))

class PersonalDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='1')
    MARITAL_CHOICES = (
        ('S', 'Single'),
        ('M', 'Married'),
        ('D', 'Divorced'),
        ('W', 'Widowed'),
    )
    marital_status = models.CharField(max_length=60, blank=True, choices=MARITAL_CHOICES)
    no_of_kids = models.IntegerField(blank=True, default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    income = models.IntegerField(blank=True, default=0,
        validators=[
            MinValueValidator(0)
        ])
    family_income = models.IntegerField(blank=True, default=0,
        validators=[
            MinValueValidator(0)
        ])
    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=256, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, blank=True, choices=GENDER_CHOICES)
    # highest_qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE, null=True, blank=True)
    ALMOST_NEVER = '5'
    SOMETIMES = '15'
    FEW_TIMES_A_MONTH = '50'
    FEW_TIMES_A_WEEK = '150'
    ALMOST_EVERYDAY = '300'
    READING_FREQUENCY_CHOICES = (
        (ALMOST_NEVER, 'Almost Never (0-5 times a year)'),
        (SOMETIMES, 'Sometimes (6-15 times a year)'),
        (FEW_TIMES_A_MONTH, 'Few times a month (Once a week)'),
        (FEW_TIMES_A_WEEK, 'Few times a week (2-4 times a week)'),
        (ALMOST_EVERYDAY, 'Almost Everyday (6 times a week)')
    )
    reading_frequency = models.CharField(max_length=50, choices=READING_FREQUENCY_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        Career.objects.create(user=instance)
        PersonalDetails.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    instance.career.save()
    instance.personaldetails.save()
