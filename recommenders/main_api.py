from recommenders.models import KeyToKeyLink, KeyToDocLink, KeyToUserLink, DocToDocLink, DocToUserLink, UserToUserLink
from interaction_system.models import BookRating

class PredictItems:

    def __init__(self, user):
        self.user = user

    # returns users
    def similar_users(self, user=self.user):
        u2u_1 = UserToUserLink.objects.filter(item1=user)
        u2u_2 = UserToUserLink.objects.filter(item2=user)
        list_of_users = []
        for x in u2u_1:
            list_of_users.append(x.item2)
        for x in u2u_2:
            list_of_users.append(x.item1)
        return list_of_users

    # returns books
    def user_items(self, user=self.user):
        # Having predict = True
        d2u = DocToUserLink.objects.filter(item2=user, stop_predict=False)
        list_of_books = []
        for d in d2u:
            list_of_books.append(d.item1)
        return list_of_books

    # returns books
    def user_liked_items(self, user=self.user):
        # Having predict = True
        br = BookRating.objects.filter(user=user, rating=1)
        list_of_books = []
        for d in br:
            list_of_books.append(d.book)
        return list_of_books

    # returns keywords
    def user_keywords(self, user=self.user):
        k2u = KeyToUserLink.objects.filter(item2=user)
        list_of_keywords = []
        for k in d2u:
            list_of_keywords.append(k.item1)
        return list_of_keywords

    # returns books
    def similar_item(self, book):
        d2d_1 = DocToDocLink.objects.filter(item1=book)
        d2d_2 = DocToDocLink.objects.filter(item2=book)
        list_of_books = []
        for x in d2d_1:
            list_of_books.append(x.item2)
        for x in d2d_2:
            list_of_books.append(x.item1)
        return list_of_books

    # returns keywords
    def keyword_items(self, keyword):
        k2u = KeyToUserLink.objects.filter(item1=keyword)
        list_of_keywords = []
        for k in k2u:
            list_of_keywords.append(k.item1)
        return list_of_keywords

    def predict(self):
        level_0_books = user_liked_items()
        level_0_1_books = []

        for x in level_0_books:
            level_0_1_books.append(similar_item(x))

        level_0_keywords = user_keywords()
        level_0_keywords_1_books = []

        for x in level_0_keywords:
            level_0_keywords_1_books.append(keyword_items(x))

        level_0_users = similar_users()
        level_0_users_1_books = []

        for x in level_0_users:
            level_0_users_1_books.append(user_liked_items(x))

        books = level_0_1_books + level_0_keywords_1_books + level_0_users_1_books

        return books
