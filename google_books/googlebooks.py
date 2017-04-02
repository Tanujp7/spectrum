import requests
import json
import random, re

class Api(object):
    """Google Books Api

    See: https://developers.google.com/books/
    """
    __BASEURL = 'https://www.googleapis.com/books/v1'
    def __init__(self ):
       pass

    def _get(self, path, params=None):
        if params is None:
            params = {}
        resp = requests.get(self.__BASEURL+path, params=params)
        if resp.status_code == 200:
            return json.loads(resp.content.decode('utf-8'))

        return resp

    def get(self, volumeId, **kwargs):
        """Retrieves a Volume resource based on ID
        volumeId -- ID of volume to retrieve.
        Optional Parameters:
        partner --  Brand results for partner ID.

        projection -- Restrict information returned to a set of selected fields.
                    Acceptable values are:
                    "full" - Includes all volume data.
                    "lite" - Includes a subset of fields in volumeInfo and accessInfo.

        source --   String to identify the originator of this request.
        See: https://developers.google.com/books/docs/v1/reference/volumes/get
        """
        path = '/volumes/'+volumeId
        params = dict()
        for p in 'partner projection source'.split():
            if p in kwargs:
                params[p] = kwargs[p]

        return self._get(path)

    def list(self, q, **kwargs):
        """Performs a book search.
        q -- Full-text search query string.

            There are special keywords you can specify in the search terms to
            search in particular fields, such as:
            intitle: Returns results where the text following this keyword is
                    found in the title.
            inauthor: Returns results where the text following this keyword is
                    found in the author.
            inpublisher: Returns results where the text following this keyword
                    is found in the publisher.
            subject: Returns results where the text following this keyword is
                    listed in the category list of the volume.
            isbn:   Returns results where the text following this keyword is the
                    ISBN number.
            lccn:   Returns results where the text following this keyword is the
                    Library of Congress Control Number.
            oclc:   Returns results where the text following this keyword is the
                    Online Computer Library Center number.
        Optional Parameters:
        download -- Restrict to volumes by download availability.
                    Acceptable values are:
                    "epub" - All volumes with epub.
        filter --   Filter search results.
                    Acceptable values are:
                    "ebooks" - All Google eBooks.
                    "free-ebooks" - Google eBook with full volume text viewability.
                    "full" - Public can view entire volume text.
                    "paid-ebooks" - Google eBook with a price.
                    "partial" - Public able to see parts of text.
        langRestrict -- Restrict results to books with this language code.
        libraryRestrict	-- Restrict search to this user's library.
                    Acceptable values are:
                    "my-library" - Restrict to the user's library, any shelf.
                    "no-restrict" - Do not restrict based on user's library.
        maxResults -- Maximum number of results to return. Acceptable values are 0 to 40, inclusive.
        orderBy	 -- Sort search results.
                    Acceptable values are:
                    "newest" - Most recently published.
                    "relevance" - Relevance to search terms.
        partner	--  Restrict and brand results for partner ID.
        printType -- Restrict to books or magazines.
                    Acceptable values are:
                    "all" - All volume content types.
                    "books" - Just books.
                    "magazines" - Just magazines.
        projection -- Restrict information returned to a set of selected fields.
                    Acceptable values are:
                    "full" - Includes all volume data.
                    "lite" - Includes a subset of fields in volumeInfo and accessInfo.

        showPreorders -- Set to true to show books available for preorder. Defaults to false.
        source --  String to identify the originator of this request.
        startIndex -- Index of the first result to return (starts at 0)
        See: https://developers.google.com/books/docs/v1/reference/volumes/list
        """
        path = '/volumes'
        params = dict(q=q)
        for p in 'download filter langRestrict libraryRestrict maxResults orderBy partner printType projection showPreorders source startIndex key'.split():
            if p in kwargs:
                params[p] = kwargs[p]

        return self._get(path, params)

def extract_details(item):
    item_dict = {
        "id" : item.get('id'),
        "title" : item.get('volumeInfo', '{}').get('title'),
        "authors" : item.get('volumeInfo', '{}').get('authors'),
        "publisher" : item.get('volumeInfo', '{}').get('publisher'),
        "published_date" : item.get('volumeInfo', '{}').get('publishedDate'),
        "isbn" : item.get('volumeInfo', '{}').get('industryIdentifiers'),
        "description" : item.get('volumeInfo', '{}').get('description'),
        "alt_description" : item.get('searchInfo', {}).get('textSnippet'),
        "page_count" : item.get('volumeInfo', '{}').get('pageCount'),
        "category" : item.get('volumeInfo', '{}').get('mainCategory'),
        "tags" : item.get('volumeInfo', '{}').get('categories'),
        "avg_rating" : item.get('volumeInfo', '{}').get('averageRating'),
        "ratings_count" : item.get('volumeInfo', '{}').get('ratingsCount'),
        "thumbnail" : item.get('volumeInfo', '{}').get('imageLinks'),
        "raw_thumbnail" : item.get('volumeInfo', '{}').get('imageLinks'),
        "language" : item.get('volumeInfo', '{}').get('language'),
        "sale_amount" : item.get('saleInfo', '{}').get('listPrice'),
        "link" : item.get('selfLink')
    }
    if item_dict['thumbnail'] is not None:
        img_url = item_dict['thumbnail'][random.choice(list(item_dict['thumbnail'].keys()))]
        img_url = re.sub('(zoom=)\w+', 'zoom=1', img_url)
        img_url = re.sub('(edge=)\w+', 'edge=uncurl', img_url)
        item_dict.update({'thumbnail' : img_url})
    if item_dict['raw_thumbnail'] is not None:
        img_url = item_dict['raw_thumbnail'][random.choice(list(item_dict['raw_thumbnail'].keys()))]
        img_url = re.sub('(zoom=)\w+', '&amp;', img_url)
        img_url = re.sub('(edge=)\w+', '&amp;', img_url)
        item_dict.update({'raw_thumbnail' : img_url})
    return item_dict

def search(query):
    api = Api()
    response = api.list(q=query, maxResults=18 , key='AIzaSyBSrnWtXVoLIBW0Ner1cQpe93tqKtFqW7g')

    items = response['items']
    result = []
    for i in items:
        result.append(extract_details(i))
    return result

def retrieve(volume_id):
    api = Api()
    book = None
    response = api.get(volumeId=volume_id)
    book = extract_details(response)
    return book
