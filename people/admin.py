from django.contrib import admin
from .models import UserProfile, Qualification, PersonalDetails

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Qualification)
admin.site.register(PersonalDetails)
