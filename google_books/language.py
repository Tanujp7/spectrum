#from oauth2client.client import GoogleCredentials
from google.cloud import language

#credentials = GoogleCredentials.get_application_default()

def request_entity(text):
    language_client = language.Client()
    document = language_client.document_from_text(text)
    response = document.analyze_entities()
    return response

def filter_entities(response):
    filtered_response = []
    for entity in response.entities:
        if entity.salience >= 0.01: filtered_response.append(entity)
    return response.entities if len(filtered_response) == 0 else filtered_response

def print_entity_details(entity):
    print('=' * 20)
    print('         name: %s' % (entity.name,))
    print('         type: %s' % (entity.entity_type,))
    print('     metadata: %s' % (entity.metadata,))
    print('     salience: %s' % (entity.salience,))

text = "Mia has come to live with her Grandma in a land of forests and snow. It isn't at all like her old life in the city, and at first she feels very different from the new children she sees. But when she watches the snow falling around her one night, Mia realises that she is just like one of the snowflakes - unique and perfect in her own way. A beautiful story about new beginnings and making friends by CBeebies presenter Cerrie Burnell."
r = filter_entities(request_entity(text))
for entity in r:
    print_entity_details(entity)
