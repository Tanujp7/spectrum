from django.contrib import admin
from .models import UserProfile, Career, PersonalDetails

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Career)
admin.site.register(PersonalDetails)
