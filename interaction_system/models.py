from django.db import models

from django.contrib.auth.models import User
from items.models import Book

class BookRating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(choices=[(i, i) for i in range(1, 6)], default=1)

    class Meta:
        unique_together = ('user', 'book')
        verbose_name = 'Book Rating'

    def __str__(self):
        return (str(self.rating) + '* - ' + str(self.book.title) + ' - rated by - ' + str(self.user))

class BookLikeDislike(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.SmallIntegerField(choices=[(i, i) for i in range(-1, 2)], default=0)

    class Meta:
        unique_together = ('user', 'book')
        verbose_name = 'Book Like/Dislike'
        verbose_name_plural = 'Book Likes/Dislikes'

    def __str__(self):
        return (str(self.like) + '* - ' + str(self.book.title) + ' - by - ' + str(self.user))

class BookInterestLog(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interest_score = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Book Interest Log'

    def __str__(self):
        return (str(self.interest_score) + '* - ' + str(self.book.title) + ' - by - ' + str(self.user))
