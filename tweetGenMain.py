import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import brown 
import pickle
import random

import tagTweets
import dictionarymaker


'''
Used http://stackoverflow.com/questions/19201290/how-to-save-a-dictionary-to-a-file
for saving object to deal with dictionary
'''

#Main Program

# dictionary of POS -> words
# 

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

# Used these lines to create data sets
#posTaggedBySentence = tagTweets.tag('tweets')
#print (posTaggedBySentence)
#save_obj(posTaggedBySentence, "tweetsPOS")

#save_obj(dictionarymaker.POSfreq(tweetsPOSList), "dictPOS")


#list of lists of tuples of type
#[[('more', 'RBR'), ('beautiful', 'JJ')], [('than', 'IN'), ('the', 'DT')]]
tweetsPOSList = load_obj("tweetsPOS")

#dict of pos -> [words freq]
dictPOS = load_obj("dictPOS")

followsPOS = {}

#these are out of 10
chanceNextPOSFirst = 5
chanceNextPOS2t5 = 3



def genTweet():
	curSym = "S#"
	generatedString = ""
	while (not len(generatedString) > 140 or curSym != "#"):
		nextSyms = followsPOS[curSym]
		chance = random.randrange(10)
		if (chance >= 5):
			nextSym = nextSyms[0]
		elif (chance >= 3):
			nextSym = nextSyms[random.randrange(1,5)]
		else:
			nextSym = nextSyms[random.randrange(5, len(nextSyms))]