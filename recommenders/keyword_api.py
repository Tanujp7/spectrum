import requests, os, nltk, math
from items.models import Key
from people.models import UserProfile
from recommenders.models import KeyToKeyLink, KeyToUserLink

class BigHugeThesaurus:

    def __init__(self, key=None):
        self.url = "http://words.bighugelabs.com/api/2/"
        self.key = key

    def request(self):

        self.url = self.url + os.environ['SPECTRUM_BIGHUGELABS_SECRET_KEY'] + '/' + str(self.key.name) + '/json'

        self.response = requests.get(self.url)
        if self.response.status_code == 200 or self.response.status_code == 301:
            return self.response.json()
        else:
            self.response = {'err':'404,500,etc'}
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

    def _get_or_create(self, keyword, weight=None):

        try:
            listing = Key.objects.get(name__iexact=str(keyword))
            listing.stop_bighuge = True
            listing.save()
        except Key.DoesNotExist:
            listing = Key.objects.create(name=str(keyword), base_level=False)

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

    def _get_or_create(self, keyword, weight=None, _type='Top Down'):

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

class NltkDistance:

    def __init__(self, key1=None, key2=None):
        self.k1 = key1
        self.k2 = key2
        self.key1 = self.key1.name
        self.key2 = self.key2.name

    def split(self,text):
        clean_text = ''.join(e for e in text if e.isalnum() or e == ' ') # Removes punctuation
        word_list = []
        for i in clean_text:
            if not i.isdigit(): # Removes digits
                word_list.append(i)
        return word_list

    def calculate(self):
        keywords1 = self.split.(self.key1)
        keywords2 = self.split.(self.key2)

        similarity_constant = 4

        minimum = 1 / math.e
        maximum = 1

        score_list = []

        for i in keywords1:
            for j in keywords2:
                x = len(i)
                y = len(j)
                distance = nltk.edit_distance(i, j)

                if ((x + y) / similarity_constant) >= distance:
                    raw_score = 2/( math.e**( x/distance ) + ( math.e**( y/distance ) ) )
                    scaled_score = (raw_score - minimum) / (maximum - minimum)
                    score_list.append(scaled_score)
        if score_list:
            return max(score_list)
        else:
            return None

    def _get(self, keyword, weight=None):

        try:
            self.k1.stop_nltkdistance = True
            self.k1.save()
            KeyToKeyLink.objects.create(item1=self.k1, item2=self.k2, raw_weight=weight, calculated_weight=weight, origin='NLTK Distance')
        except Key.DoesNotExist:
            pass

    def analyse(self):

        score = self.calculate()
        if score is not None and score >= 0.4:
            self._get(k, weight=score)

        return score

def api_call(key):

    def big(key):
        if key.base_level is True:
            if not key.stop_bighuge:
                print('Calling Synonym BigHugeThesaurus API..')
                k = BigHugeThesaurus(key=key)
                k.analyse()
                key.stop_bighuge = True
                key.save()

    def words(key):
        if key.base_level is True:
            if not key.stop_wordsapi:
                print('Calling Symantec WordsAPI..')
                k = WordsAPI(key=key)
                k.analyse()
                key.stop_wordsapi = True
                key.save()

    # Schedule Jobs here..
    print('Attempt...')
    big(key)
    words(key)
    print('Completed.')

def nltk_distance(key1,key2):
    if not key1.stop_nltkdistance:
        if not Key.objects.filter(item1=key1, item2=key2, origin='NLTK distance') and not Key.objects.filter(item1=key2, item2=key1, origin='NLTK distance'):
            print('Calling NLTK distance..')
            k = NltkDistance(key1, key2)
            k.analyse()

def destroy_k2u_links(keys, user):

    for k in keys:
        try:
            element = KeyToUserLink.objects.get(item1__name__iexact=str(k), item2=user, raw_weight=weight, calculated_weight=weight, origin='User Interest/Career')
            element.delete()
        except KeyToUserLink.DoesNotExist:
            pass

def add_k2u_links_by_key(keys, user):

    weight = 0.8
    for k in keys:
        try:
            listing = Key.objects.get(name__iexact=str(k))
        except Key.DoesNotExist:
            listing = Key.objects.create(name=str(k))

        KeyToUserLink.objects.create(item1=listing, item2=user, raw_weight=weight, calculated_weight=weight, origin='User Interest/Career')

def add_k2u_links_by_user(user):

    weight = 0.8
    keys = [x.keyword for x in user.interest_keywords.all()] + [x.keyword for x in user.career_keywords.all()]
    for k in keys:
        if KeyToUserLink.objects.get(item1__name__iexact=str(k), item2=user, origin='User Interest/Career'):
            try:
                listing = Key.objects.get(name__iexact=str(k))
            except Key.DoesNotExist:
                listing = Key.objects.create(name=str(k))

            KeyToUserLink.objects.create(item1=listing, item2=user, raw_weight=weight, calculated_weight=weight, origin='User Interest/Career')

def user_migration():
    user_list = UserProfile.objects.all()
    for u in user_list:
        print('User : ' + str(u))
        try:
            add_k2u_links_by_user(u)
            print('Linked keywords.')
        except:
            pass

def migration():

    keyword_list = Key.objects.all()

    for keyword in keyword_list:
        print('Keyword : ' + str(keyword))
        api_call(keyword)
        print('-- next() --> ? ')

    print('-- All Tasks Completed --')
