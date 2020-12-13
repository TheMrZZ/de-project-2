import multiprocessing
import re
from os import path

import pandas as pd
from gensim.models.doc2vec import TaggedDocument, Doc2Vec
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.tokenizer import Tokenizer

nlp = English()
# Create a blank Tokenizer with just the English vocab
tokenizer = Tokenizer(nlp.vocab)

MODEL_FILE_NAME = 'model_file'


def normalize(text, remove_stopwords):
    # Lower
    text = text.lower()

    # Remove pictures
    regex = r'pic\.twitter\.com.*'
    text = re.sub(regex, '', text, 0, re.MULTILINE)

    text = nlp(text)
    lemmatized = list()

    # Lemmatize & remove stopwords
    for word in text:
        lemma = word.lemma_.strip()
        if lemma:
            if not remove_stopwords or lemma not in STOP_WORDS:
                lemmatized.append(lemma)

    return " ".join(lemmatized)


def remove_punctuation(tokens):
    return [t for t in tokens if not t.is_punct or t.is_space]


def process(text, *, remove_stopwords=False, remove_punct=False):
    norm = normalize(text, remove_stopwords)
    tokens = list(tokenizer(norm))
    if remove_punct:
        tokens = remove_punctuation(tokens)
    return [str(token) for token in tokens]


def load_model():
    return Doc2Vec.load(MODEL_FILE_NAME)


def main():
    # IMPORT DATA
    current_dir = path.dirname(__file__)

    data = pd.read_csv(path.join(current_dir, 'tweets.csv'))
    data.loc[:, 'tokens'] = data.text.apply(process)

    sentences = []
    for i, tweet_tokens in enumerate(data['tokens'].values.tolist()):
        sentences.append(TaggedDocument(tweet_tokens, [i]))

    # MODEL PARAMETERS
    size = 300
    context_window = 50
    min_count = 1
    max_iter = 200

    # BUILD MODEL
    model = Doc2Vec(
        documents=sentences,
        min_count=min_count,  # ignore words with freq less than min_count
        max_vocab_size=None,
        window=context_window,  # the number of words before and after to be used as context
        size=size,  # is the dimensionality of the feature vector
        workers=multiprocessing.cpu_count(),
        iter=max_iter  # number of iterations (epochs) over the corpus)
    )

    model.save(MODEL_FILE_NAME)


if __name__ == '__main__':
    main()
