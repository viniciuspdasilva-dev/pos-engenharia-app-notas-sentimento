import nltk
from nltk.corpus import stopwords


class SentimentAnalysis:
    def __init__(self, train_list: [[str, str]]):
        self.train_list = train_list
        self.__init_nltk__()

    def train(self, words):
        frasesStemming = self.aplic_stemmer(words)
        words_train = self.find_words(frasesStemming)


    def find_words(self, frases):
        words = []
        for (palavra, sentimento) in frases:
            words.extend((palavra, sentimento))
        return words

    def aplic_stemmer(self, text):
        self.stemmer = nltk.stem.RSLPStemmer()
        frases = []
        for (palavra, sentimento) in text:
            stem = [str(self.stemmer.stem(palavra)) for p in palavra.split() if p not in self.stopwords]
            frases.append((stem, sentimento))
        return frases

    def frequency(self, words):
        words = nltk.FreqDist(words)
        return words

    def find_unique_word(self, words):
        freq = self.frequency(words)
        return freq.keys()

    def extract(self, documento, unique_words):
        doc = set(documento)
        caracteres = []
        for p in unique_words:
            caracteres['%s ' % p] = (p in doc)
        return caracteres

    def __init_nltk__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('rslp')
        stopwords = nltk.corpus.stopwords.words('portuguese')
        stopwords.remove('não')
        stopwords.remove('nao')
        stopwords.append('vou')
        stopwords.append('tão')
        self.stopwords = stopwords
        print(self.stopwords)