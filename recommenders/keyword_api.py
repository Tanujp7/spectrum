import requests
import os

from items.models import Key
from recommenders.models import KeyToKeyLink

class BigHugeThesaurus(key=None):

    self.url = "http://words.bighugelabs.com/api/2/"
    self.key = key


    def request(self):

        self.url = self.url + os.environ['SPECTRUM_BIGHUGELABS_SECRET_KEY'] + '/' + self.key + '/json'

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


    def _get_or_create(self, keyword, weight=0.5):

        try:
            listing = Key.objects.get(name__iexact=str(keyword))
        except Key.DoesNotExist:
            listing = Key.objects.create(name=str(keyword))

        KeyToKeyLink.objects.create(item1=listing, item2=self.key, raw_weight=weight, calculated_weight=weight, origin='BigHuge Synonyms')

        return listing


    def analyse(self):

        response = self.filter()

        for k in response:
            self._get_or_create(k)

        return response


class WordsAPI(key=None):

    self.url = "https://wordsapiv1.p.mashape.com/words/"
    self.key = key


    def request(self):

        self.url = self.url + self.key
        self.response = requests.get( self.url,
                                      headers={
                                        "X-Mashape-Key": os.environ['SPECTRUM_MASHAPE_SECRET_KEY'],
                                        "Accept": "application/json"
                                      }
                                    ).json()
        return self.response


    def filter(self):

        raw_response = self.request()
        typeof_response = []
        hastypes_response = []

        if raw_response.get('results'):
            for result in raw_response.get('results'):
                if result.get('typeOf'):
                    for word in result.get('typeOf'):
                        typeof_response.append(str(word))
                if result.get('hasTypes'):
                    for word in result.get('hasTypes'):
                        hastypes_response.append(str(word))

        return typeof_response, hastypes_response


    def _get_or_create(self, keyword, weight=0.5, _type='Top Down'):

        try:
            listing = Key.objects.get(name__iexact=str(keyword))
        except Key.DoesNotExist:
            listing = Key.objects.create(name=str(keyword))

        KeyToKeyLink.objects.create(item1=listing, item2=self.key, raw_weight=weight, calculated_weight=weight, origin='WordsAPI Symantec Relatedness '+ _type)

        return listing


    def analyse(self):

        typeof_response, hastypes_response = self.filter()

        for k in typeof_response:
            self._get_or_create(k, 0.65, 'Bottom Up')
        for k in hastypes_response:
            self._get_or_create(k, 0.35, 'Top Down')

        return (typeof_response + hastypes_response)


def api_call(key):

    def big(key):

        print('Calling Synonym BigHugeThesaurus API..')
        with BigHugeThesaurus(key=key) as k:
            k.analyse()
            print(', '.join(k))

    def words(key):

        print('Calling Symantec WordsAPI..')
        with WordsAPI(key=key) as k:
            k.analyse()
            print(', '.join(k))

    # Schedule Jobs here..
    print('Calling attempt...')
    big(key)
    words(key)
    print('Calling completed.')

def migration():

    keyword_list = Key.objects.all()

    for keyword in keyword_list:
        print('Keyword : ' + str(keyword.name))
        api_call(keyword.name)
        print('-- next() --> ? ')

    print('-- All Tasks Completed --')
