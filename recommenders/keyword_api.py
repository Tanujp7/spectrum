import requests
import os

from items.models import Key
from recommenders.models import KeyToKeyLink

class BigHugeThesaurus(key=None):

    self.url = "http://words.bighugelabs.com/api/2/"
    self.key = key


    def request(self):

        self.url = self.url + os.environ['SPECTRUM_BIGHUGELABS_SECRET_KEY'] + '/' + self.key + '/json/'

        self.response = requests.get(self.url).json()
        return self.response


    def filter(self):

        raw_response = self.request()
        response = []

        if raw_response.get('noun'):
            for word in raw_response.get('noun').get('syn', []):
                response.append(str(word))
            for word in raw_response.get('noun').get('sim', []):
                response.append(str(word))
            for word in raw_response.get('noun').get('rel', []):
                response.append(str(word))
        if raw_response.get('verb'):
            for word in raw_response.get('verb').get('syn', []):
                response.append(str(word))
            for word in raw_response.get('verb').get('sim', []):
                response.append(str(word))
            for word in raw_response.get('verb').get('rel', []):
                response.append(str(word))

        return response


    def _get_or_create(self, keyword):

        try:
            listing = Key.objects.get(name__iexact=str(keyword))
        except Key.DoesNotExist:
            listing = Key.objects.create(name=str(keyword))

        KeyToKeyLink.objects.create(item1=listing, item2=self.key, raw_weight=float(0.5), calculated_weight=(float(0.5)), origin='BigHuge Synonyms')

        return listing


    def analyse(self):

        response = self.filter()

        for k in response:
            self._get_or_create(k)

        return response
