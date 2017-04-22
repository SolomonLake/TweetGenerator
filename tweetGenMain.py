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

#need to order these by freq

#dict of pos -> [[words freq]]
dictPOS = load_obj("dictPOS")

#dict of pos -> [[POS freq]]
followsPOS = {}

#these are out of 10
chanceNextFirst = 5
chanceNext2t5 = 3



def genTweet():
	curSym = "S#"
	generatedString = ""
	while (not len(generatedString) > 140 or curSym != "#"):
		if (curSym != "S#"):
			chancePOS = random.randrange(10)
			if (chancePOS >= chanceNextPOSFirst):
				whichWord = random.randrange(int(len(dictPOS[curSym])/10))
				generatedString += dictPOS[curSym][whichWord][0]
			elif (chancePOS >= chanceNextPOS2t5):
				whichWord = random.randrange(int(len(dictPOS[curSym])/10), int(len(dictPOS[curSym])/3))
				curSym = nextSyms[random.randrange(1,5)]
			else:
				whichWord = random.randrange(int(len(dictPOS[curSym])/3), len(dictPOS[curSym]))
				generatedString += dictPOS[curSym][random.randrange[len(dictPOS[curSym])]]

		nextSyms = followsPOS[curSym]
		chanceSym = random.randrange(10)
		if (chanceSym >= chanceNextPOSFirst):
			curSym = nextSyms[0][0]
		elif (chanceSym >= chanceNextPOS2t5):
			curSym = nextSyms[random.randrange(1,5)][0]
		else:
			curSym = nextSyms[random.randrange(5, len(nextSyms))][0]

	print (generatedString)
