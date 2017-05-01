from django.contrib import admin
from .models import KeyToKeyLink, KeyToDocLink, KeyToUserLink, DocToDocLink, DocToUserLink, UserToUserLink

# Register your models here.
admin.site.register(KeyToKeyLink)
admin.site.register(KeyToDocLink)
admin.site.register(KeyToUserLink)
admin.site.register(DocToDocLink)
admin.site.register(DocToUserLink)
admin.site.register(UserToUserLink)
