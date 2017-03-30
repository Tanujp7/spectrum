from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Qualification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='3')
    qualification_name = models.CharField(max_length=60, blank=True, default='student')
    qualification_stream = models.CharField(max_length=60, blank=True, default='student')

    def __str__(self):
        return (self.qualification_name + ' ' + self.qualification_stream)

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
    occupation = models.CharField(max_length=100, blank=True)
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
        Qualification.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
    instance.qualification.save()
