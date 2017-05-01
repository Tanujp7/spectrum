from google.cloud import language # For Google Cloud : Natural Language
import requests # For MeaningCloud
import os # For Key (inside Environment variable)

from items.models import Key
from recommenders.models import KeyToDocLink

class GoogleEntity(document=None):

    self.document = document
    self.query_text = (lambda document.book.title: str(document.book.title) or '') + ' | ' + (lambda document.description: str(document.description) or '') if document else ''


    def request(self):

        language_client = language.Client()
        document = language_client.document_from_text(self.query_text)
        self.response = document.analyze_entities()


    def filter(self):

        self.request()
        filtered_response = []
        for entity in self.response.entities:
            # Threshold value is set to 0.01 to exclude irreleveant entities
            if float(entity.salience) >= 0.01: filtered_response.append(entity)

        return self.response.entities if len(filtered_response) == 0 else filtered_response


    def _get_or_create(self, entity):

        try:
            listing = Key.objects.get(name__iexact=entity.name)
        except Key.DoesNotExist:
            listing = Key.objects.create(name=entity.name)

        KeyToDocLink.objects.create(item1=listing, item2=self.document, raw_weight=float(entity.salience), calculated_weight=float(entity.salience), origin='Entity Analysis')

        return listing


    def analyse(self):

        response = self.filter()
        self.entities = []
        for entity in response:
            self.entities.append(self._get_or_create(entity))

        return self.entities

class MeaningCloudClassifier(document=None):

    self.url = "http://api.meaningcloud.com/class-1.1"
    self.document = document


    def request(self):

        payload = 'key=' + os.environ['SPECTRUM_MEANINGCLOUD_SECRET_KEY'] + '&txt=' + self.document.description + '&title=' + self.document.book.title + '&model=IPTC_en'
        headers = {'content-type': 'application/x-www-form-urlencoded'}

        self.response = requests.request("POST", self.url, data=payload, headers=headers).json()
        return self.response


    def _get_or_create(self, category):

        try:
            listing = Key.objects.get(name__iexact=str(category.get('label')))
        except Key.DoesNotExist:
            listing = Key.objects.create(name=str(category.get('label')))

        KeyToDocLink.objects.create(item1=listing, item2=self.document, raw_weight=float(category.get('abs_relevance')), calculated_weight=(float(category.get('relevance'))/100.00), origin='IPTC Classification')

        return listing


    def analyse(self):

        response = self.request()

        if response.get(status, default={'code':'666',}).get('code') == '0':

            self.category = []
            for cat in response.get('category_list'):
                self.category.append(self._get_or_create(cat))

        return self.category