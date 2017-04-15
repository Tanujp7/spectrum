from django.db import models

from django.contrib.auth.models import User
from items.models import Book

from django_pandas.managers import DataFrameManager

class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(choices=[(i, i) for i in range(0, 2)], default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = DataFrameManager()

    class Meta:
        unique_together = ('user', 'book')
        verbose_name = 'Book Rating'

    def __str__(self):
        return (str(self.rating) + ' on ' + str(self.book.title) + ' by ' + str(self.user) + ' at ' + str(self.created_at))
