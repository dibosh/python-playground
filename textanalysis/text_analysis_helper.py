import json
import os
import re

from stemming.porter2 import stem
from textblob import TextBlob

dir_path = os.path.dirname(os.path.realpath(__file__))


def get_stop_words():
    with open(dir_path + '/stopwords.txt') as fp:
        return fp.read().replace('\n', ' ').split(' ')


def get_context_words():
    with open(dir_path + '/context-words.txt') as fp:
        return fp.read().replace('\n', ' ').split(' ')


def get_stemmed_context_words():
    return [stem(word) for word in get_context_words()]


def sanitized_words(sentence):
    alpha_numeric_char_pattern = re.compile('[^a-zA-Z0-9]')
    stop_words = get_stop_words()
    return [alpha_numeric_char_pattern.sub('', word) for word in sentence.split(' ') if word not in stop_words]


def get_matched_context_words(sentence):
    return [word for word in sanitized_words(sentence) if stem(word).lower() in get_stemmed_context_words()]


def get_sentiment_polarity(sentence):
    return TextBlob(sentence).sentences[0].sentiment.polarity


def get_brands():
    with open(dir_path + '/brands.json') as fp:
        return json.load(fp)['brands']
