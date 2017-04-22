import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import brown 

#def tag(tweet):
#  for word in tweet:

def tag(filename):
  # Get list of tweets. Each tweet is list of words. 
  tokenized_tweets = []
  tagged_tweets = []
  with open(filename) as f:
    content = [x.strip('\n') for x in f.readlines()]
    content = list(set(content)-set(['']))
    tokenized_tweets = [word_tokenize(i) for i in content]

  for tweet in tokenized_tweets:
    tagged_tweets.append(nltk.pos_tag(tweet))

  return tagged_tweets

'''  
  # tag each word with most likely tag
  text = [] 
  for tweet in tokenized_tweets:
    taggedTweet = []
    for i in range(len(tweet)):
      tag = (tweet[i],MostLikelyTag(tweet[i]))
      taggedTweet.append(tag)
    text.append(taggedTweet)

  return text
'''
  
print tag('tweets')
