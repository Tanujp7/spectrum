from django.db import models

from django.contrib.auth.models import User
from items.models import Book

class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(choices=[(i, i) for i in range(-1, 2)], default=0)

    class Meta:
        unique_together = ('user', 'book')
        verbose_name = 'Book Rating'

    def __str__(self):
        return (str(self.rating) + '* - ' + str(self.book.title) + ' - rated by - ' + str(self.user))

class RatingLog(models.Model):
    book_rating = models.ForeignKey(BookRating, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(choices=[(i, i) for i in range(-1, 2)], default=0)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (str(self.rating) + '* - ' + str(self.book_rating.book.title) + ' -  by - ' + str(self.book_rating.user))
