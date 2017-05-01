"""
# Note #
This file is only meant to be run once. To migrate old models (BookProfile) into API compatible ones.
"""

from items.models import BookProfile
from recommenders.language_api import GoogleEntity, MeaningCloudClassifier

def api_call(document):

    def gnlp(document):
        if not document.stop_gnlp:
            print('Calling Google Natural Language API..')
            entities = GoogleEntity(document=document)
            entities.analyse()
            document.stop_gnlp = True
            document.save()

    def meaningcloud(document):
        if not document.stop_meaningcloud:
            print('Calling MeaningCloud Text Classification API..')
            iptc_label = MeaningCloudClassifier(document=document)
            iptc_label.analyse()
            document.stop_meaningcloud = True
            document.save()

    # Schedule Jobs here..
    print('Calling attempt...')
    gnlp(document)
    meaningcloud(document)
    print('Calling completed.')

def migration():

    book_list = BookProfile.objects.all()

    for book in book_list:
        print('Book : ' + str(book.book))
        api_call(book)
        print('-- next() --> ? ')

    print('-- All Tasks Completed --')
