"""
# Note #
This file is only meant to be run once. To migrate old models (BookProfile) into API compatible ones.
"""

from items.models import BookProfile
from recommenders.language_api import GoogleEntity, MeaningCloudClassifier

def api_call(document):

    def gnlp(document):

        print('Calling Google Natural Language API..')
        with GoogleEntity(document=document) as entities:
            entities.analyse()
            print(', '.join(entities))

    def meaningcloud(document):

        print('Calling MeaningCloud Text Classification API..')
        with MeaningCloudClassifier(document=document) as iptc_label:
            iptc_label.analyse()
            print(', '.join(iptc_label))

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
