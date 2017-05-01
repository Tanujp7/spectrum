import requests
import os

from items.models import Key
from recommenders.models import KeyToKeyLink


class BigHugeThesaurus:


    def __init__(self, key=None):
        self.url = "http://words.bighugelabs.com/api/2/"
        self.key = key

    def request(self):

        self.url = self.url + os.environ['SPECTRUM_BIGHUGELABS_SECRET_KEY'] + '/' + str(self.key.name) + '/json'

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
            listing.stop_bighuge = True
            listing.save()
        except Key.DoesNotExist:
            listing = Key.objects.create(name=str(keyword), stop_bighuge=True)

        KeyToKeyLink.objects.create(item1=listing, item2=self.key, raw_weight=weight, calculated_weight=weight, origin='BigHuge Synonyms')

        return listing


    def analyse(self):

        response = self.filter()

        for k in response:
            self._get_or_create(k)

        return response


class WordsAPI:

    def __init__(self, key=None):
        self.url = "https://wordsapiv1.p.mashape.com/words/"
        self.key = key


    def request(self):

        self.url = self.url + str(self.key.name)
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
            listing.stop_wordsapi = True
            listing.save()
        except Key.DoesNotExist:
            listing = Key.objects.create(name=str(keyword), stop_wordsapi=True)

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
        if not key.stop_bighuge:
            print('Calling Synonym BigHugeThesaurus API..')
            k = BigHugeThesaurus(key=key)
            k.analyse()
            k.stop_bighuge = True
            k.save()
        print('Skipping Synonym BigHugeThesaurus API..')

    def words(key):
        if not key.stop_wordsapi:
            print('Calling Symantec WordsAPI..')
            k = WordsAPI(key=key)
            k.analyse()
            k.stop_wordsapi = True
            k.save()
        print('Skipping Symantec WordsAPI..')

    # Schedule Jobs here..
    print('Calling attempt...')
    big(key)
    words(key)
    print('Calling completed.')


def migration():

    keyword_list = Key.objects.all()

    for keyword in keyword_list:
        print('Keyword : ' + str(keyword))
        api_call(keyword)
        print('-- next() --> ? ')

    print('-- All Tasks Completed --')
