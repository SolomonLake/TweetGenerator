import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import brown 
from nltk.util import ngrams


def tag(filename):
  # Get list of tweets. Each tweet is list of words. 
  tokenized_tweets = []
  tagged_tweets = []
  trigrams = []
  with open(filename) as f:
    #content = [x.strip('\n') for x in f.readlines()]
    content = [x.replace('\n','~ ^') for x in f.readlines()]
    content.insert(0,'^ ')
    content = list(set(content[:-1])-set(['']))
    tokenized_tweets = [word_tokenize(i) for i in content]

  for tweet in tokenized_tweets:
    tagged_tweets.append(nltk.pos_tag(tweet))
    trigrams.append(ngrams(tweet,3))     

  #http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
  trigrams = [item for sublist in trigrams for item in sublist]

  # used to return tagged_tweets
  return trigrams

  
print tag('tweets')
