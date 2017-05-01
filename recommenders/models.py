from django.db import models

from items.models import Key, BookProfile
from people.models import UserProfile

class Link(models.Model):
    raw_weight = models.FloatField()
    calculated_weight = models.FloatField()
    origin = models.CharField(max_length=512, null=True, blank=True, default=None)

    class Meta:
        abstract = True

class KeyToKeyLink(Link):
    item1 = models.ForeignKey(Key, related_name='%(class)s_item1')
    item2 = models.ForeignKey(Key, related_name='%(class)s_item2')

    def __str__(self):
        return (str(self.item1) + ' | ' + str(self.item1) + ' w = ' + str(self.weight) + ' origin : ' + str(self.origin))


class KeyToDocLink(Link):
    item1 = models.ForeignKey(Key)
    item2 = models.ForeignKey(BookProfile)

    def __str__(self):
        return (str(self.item1) + ' | ' + str(self.item1) + ' w = ' + str(self.weight) + ' origin : ' + str(self.origin))


class KeyToUserLink(Link):
    item1 = models.ForeignKey(Key)
    item2 = models.ForeignKey(UserProfile)

    def __str__(self):
        return (str(self.item1) + ' | ' + str(self.item1) + ' w = ' + str(self.weight) + ' origin : ' + str(self.origin))


class DocToDocLink(Link):
    item1 = models.ForeignKey(BookProfile, related_name='%(class)s_item1')
    item2 = models.ForeignKey(BookProfile, related_name='%(class)s_item2')

    def __str__(self):
        return (str(self.item1) + ' | ' + str(self.item1) + ' w = ' + str(self.weight) + ' origin : ' + str(self.origin))


class DocToUserLink(Link):
    item1 = models.ForeignKey(BookProfile)
    item2 = models.ForeignKey(UserProfile)

    def __str__(self):
        return (str(self.item1) + ' | ' + str(self.item1) + ' w = ' + str(self.weight) + ' origin : ' + str(self.origin))


class UserToUserLink(Link):
    item1 = models.ForeignKey(UserProfile, related_name='%(class)s_item1')
    item2 = models.ForeignKey(UserProfile, related_name='%(class)s_item2')

    def __str__(self):
        return (str(self.item1) + ' | ' + str(self.item1) + ' w = ' + str(self.weight) + ' origin : ' + str(self.origin))
