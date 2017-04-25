from google.cloud import language

from items.models import Entity

def request_entity(text):

    language_client = language.Client()
    document = language_client.document_from_text(text)
    response = document.analyze_entities()

    return response

def filter_entities(response):

    filtered_response = []
    for entity in response.entities:
        # Threshold value is set to 0.01 to exclude irreleveant entities
        if entity.salience >= 0.01: filtered_response.append(entity)

    return response.entities if len(filtered_response) == 0 else filtered_response

def get_or_create_entity(entity):

    try:
        listing = Entity.objects.get(name__iexact=entity.name, kind=entity.entity_type)

    except Entity.DoesNotExist:
        Entity.objects.create(name=entity.name, kind=entity.entity_type)
        listing = Entity.objects.get(name__iexact=entity.name, kind=entity.entity_type)

    return listing
