import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import brown 
from nltk.util import bigrams
import pickle

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)



def tag(filename):
  # Get list of tweets. Each tweet is list of words. 
  tokenized_tweets = []
  tagged_tweets = []
  #bgs = []
  with open(filename) as f:
    #content = [x.strip('\n') for x in f.readlines()]
    content = [x.replace('\n',' ~ S ^ ') for x in f.readlines()]
    content.insert(0,' S ^ ')
    content = list(set(content)-set(['']))
    tokenized_tweets = [word_tokenize(i) for i in content]

  tokenized_tweets = [item for sublist in tokenized_tweets for item in sublist]
  #for tweet in tokenized_tweets:
    #tagged_tweets.append(nltk.pos_tag(tweet))
  bgs = list(bigrams(tokenized_tweets))

  #http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
  #bgs = [item for sublist in bgs for item in sublist]
  #print bgs

  bigram_tweets = {el:{} for el in bgs}
  for i in range (0, len(bgs)):
    print bgs[i]
    for key in bigram_tweets:
      if bgs[i][0] == key[1]:
        if bgs[i] in bigram_tweets[key]:
          bigram_tweets[key][bgs[i]] += 1
        else:
          bigram_tweets[key][bgs[i]] = 1
  



  #print bigram_tweets
  print bigram_tweets[('Debate','polls')]
   

  save_obj(bigram_tweets, "bigram_tweets")
  return
  # used to return tagged_tweets
  #return bgs

  
tag('tweets')


"""
if bgs[i] not in bigram_tweets:
  if i == len(bgs) - 1:
    bigram_tweets[bgs[i]] = {}
  else:
    bigram_tweets[bgs[i]] = {bgs[i+1]: 1}
else:
  if i == len(bgs) - 1:
    bigram_tweets[bgs[i]] = bigram_tweets[bgs[i]]
  else:
    if bgs[i+1] in bigram_tweets[bgs[i]]:
      bigram_tweets[bgs[i]][bgs[i+1]] += 1
    else:
      bigram_tweets[bgs[i]][bgs[i+1]] = 1
"""