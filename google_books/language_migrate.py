"""
# Note #
This file is only meant to be run once. To migrate old models (BookProfile) into Natural Language compatible ones.
"""

from items.models import BookProfile
from . import language as gnlp

def request_gnlp(description):
    language_analysis = gnlp.filter_entities(gnlp.request_entity(description))
    entity_objects = []
    for entity in language_analysis:
        entity_objects.append(gnlp.get_or_create_entity(entity))
    return entity_objects

def bulk_migrate():
    old_entries = BookProfile.objects.filter(entities=None)

    for book in old_entries:
        print('Fetching ' + str(book.book) + '...')
        entity_objects = request_gnlp(book.description)
        if len(entity_objects) > 0:
            book.entities.add(*entity_objects)
        book.save()
        print('Saving ' + str(book.book) + '...')
    print('Done!')
