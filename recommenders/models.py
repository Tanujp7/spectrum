from django.db import models

from items.models import Key, BookProfile
from people.models import UserProfile

class Link(models.Model):
    raw_weight = models.FloatField()
    calculated_weight = models.FloatField()
    origin = models.CharField(max_length=512, null=True, blank=True, default=None)

    def __str__(self):
        if hasattr(self, "item1") and hasattr(self, "item2") and isinstance(self.item1, models.Field) and isinstance(self.item2, models.Field):
            return (str(self.item1) + ' | ' + str(self.item1) + ' w = ' + self.weight + ' origin : ' + self.origin)

    class Meta:
        abstract = True

class KeyToKeyLink(Link):
    item1 = models.ForeignKey(Key)
    item2 = models.ForeignKey(Key)

class KeyToDocLink(Link):
    item1 = models.ForeignKey(Key)
    item2 = models.ForeignKey(BookProfile)

class KeyToUserLink(Link):
    item1 = models.ForeignKey(Key)
    item2 = models.ForeignKey(UserProfile)

class DocToDocLink(Link):
    item1 = models.ForeignKey(BookProfile)
    item2 = models.ForeignKey(BookProfile)

class DocToUserLink(Link):
    item1 = models.ForeignKey(BookProfile)
    item2 = models.ForeignKey(UserProfile)

class UserToUserLink(Link):
    item1 = models.ForeignKey(UserProfile)
    item2 = models.ForeignKey(UserProfile)
