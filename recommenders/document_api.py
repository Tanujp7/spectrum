import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer
from items.models import BookProfile
from recommenders.models import DocToDocLink

class DocumentSimilarity:

    def __init__(self, doc1=None, doc2=None):
        self.b1 = doc1
        self.b2 = doc2

    def calculate_cosine(self):
        stemmer = nltk.stem.porter.PorterStemmer()
        clean_punc = dict((ord(char), None) for char in string.punctuation)

        def stem_tokens(tokens):
            return [stemmer.stem(item) for item in tokens]

        #remove punctuation, lowercase, stem
        def normalize(text):
            return stem_tokens(nltk.word_tokenize(text.lower().translate(clean_punc)))

        documents = [self.b1.book.description, self.b2.book.description]
        tfidf = TfidfVectorizer(tokenizer=normalize, stop_words='english').fit_transform(documents)
        pairwise_cosine_similarity = (tfidf * tfidf.T).A
        score = pairwise_cosine_similarity[0][1]
        return score

    def _get(self, weight=None):

        DocToDocLink.objects.create(item1=self.b1, item2=self.b2, raw_weight=weight, calculated_weight=weight, origin='TFIDF Document Similarity')

    def analyse(self):

        score = self.calculate_cosine()
        if score >= 0.5:
            self._get(weight=score)


def migrate_d2d():
    books = BookProfile.objects.all()

    for i in books:
        for j in books:
            if i.book.volume_id != j.book.volume_id:
                if not i.stop_docsim:
                    print('Initiating TF-IDF Document Similarity..')
                    d = DocumentSimilarity(doc1=i,doc2=j)
                    d.analyse()
        i.stop_docsim = True
        i.save()
