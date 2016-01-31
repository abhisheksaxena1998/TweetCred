import pandas as pd
from pandas import DataFrame
import datetime
import pandas.io.data
from __future__ import division  # Python 2 users only
import nltk, re, pprint
from nltk import word_tokenize

def hashtags(text):
	for i in range(0,len(text)):
		raw = text[i].decode('utf-8')
		tokens = word_tokenize(raw)
		x = tokens.count('#')
		df['hashtag_count'][i] = x
	print 'Hashtag Count Calculated!'


def hashtags(text):
	raw = text.decode('utf-8')
	tokens = word_tokenize(raw)
	x = tokens.count('#')
	return x

df['hashtag_count'] = map(hashtags, df['text'])

def mentions(text):
    raw = text.decode('utf-8')
    tokens = word_tokenize(raw)
    x = tokens.count('@')
    return x


df['mentions_count'] = map(mentions, df['text'])


y = re.findall(r'[:]+[)*]|[:][(*]|[:][d*]|[:][p*]|[;][d*]|[:][o*]|[;][)*]|[;][(*]|[;][d*]|[;][p*]|[;][o*]', x)

def emoticons(text):
	raw = text.decode('utf-8')
	raw = raw.strip().replace(' ', '').lower()
	y = re.findall(r'[:]+[)*]|[:][(*]|[:][d*]|[:][p*]|[;][d*]|[:][o*]|[;][)*]|[;][(*]|[;][d*]|[;][p*]|[;][o*]', raw)
	print len(y)


# replace hyperlinks with URL
# keep URL link separately
# count number of URL in text
# calculate WOT score for the URL, store as separate feature




