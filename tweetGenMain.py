import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import brown 
import pickle
import random
import math

#import tagTweets
import dictionarymaker


'''
Used http://stackoverflow.com/questions/19201290/how-to-save-a-dictionary-to-a-file
for saving object to deal with dictionary

Used http://stackoverflow.com/questions/17555218/python-how-to-sort-a-list-of-lists-by-the-fourth-element-in-each-list
for list sort function
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
#save_obj(tagTweets.tag('tweets'), "tweetsPOS")
#save_obj(dictionarymaker.POSfreq(tweetsPOSList), "dictPOS")


#list of lists of tuples of type
#[[('more', 'RBR'), ('beautiful', 'JJ')], [('than', 'IN'), ('the', 'DT')]]
tweetsPOSList = load_obj("tweetsPOS")

biTweets = load_obj("bigram_tweets")


#dict of pos -> [[words freq]]
dictPOS = load_obj("dictPOS")

#dict of pos -> [[POS freq]]
followsPOS = load_obj("followsPOS")

#need to order these by freq
for unsorted_list in dictPOS.values():
	unsorted_list.sort(key=lambda x: x[1])
for unsorted_list in followsPOS.values():
	unsorted_list.sort(key=lambda x: x[1])

#these are out of 10
chanceNextFirst = 5
chanceNext2t5 = 3


puncSyms = ["!", ".", "?"]
noSpaceAfter = ['#', '@']

def genTweet():
	#startGrams = [x for x in biTweets if x[0] == "^"]
	generatedString = ""
	curGram = random.choice(biTweets[('S','^')].keys())
	generatedString += curGram[1] + " "

	while (len(generatedString) < 140):
		curGram = random.choice(biTweets[curGram].keys())
		if curGram[1] == '~':
			break
		if curGram[1] in puncSyms:
			generatedString = generatedString[:-1]
		if curGram[1] not in noSpaceAfter:
			generatedString += curGram[1] + " "
		else:
			generatedString += curGram[1]

	"""
	curSym = "^"
	generatedString = ""
	while (len(generatedString) < 140 and curSym != "~"):
		if (curSym != "^"):
			chancePOS = random.randrange(10)
			#print(curSym)
			#print(generatedString)
			#print(len(generatedString) < 140)
			#print(dictPOS[curSym])
			#print(len(dictPOS[curSym]))
			nextWord = ""
			if (chancePOS >= chanceNextFirst or len(dictPOS[curSym]) == 1):
				val = math.ceil(len(dictPOS[curSym])/10.0)
				#print (len(dictPOS[curSym]))
				#print (val)
				whichWord = random.randrange(val)
				nextWord = dictPOS[curSym][whichWord][0] + " "
			elif (chancePOS >= chanceNext2t5):
				whichWord = random.randint(math.ceil(len(dictPOS[curSym])/10.0), math.ceil(len(dictPOS[curSym])/3.0))
				#print(whichWord)
				nextWord = dictPOS[curSym][whichWord][0] + " "
			else:
				whichWord = random.randrange(math.ceil(len(dictPOS[curSym])/3), len(dictPOS[curSym])+1)
				nextWord = dictPOS[curSym][random.randrange(len(dictPOS[curSym]))][0] + " "
			generatedString += nextWord
			if (nextWord in endOfWordPunc):
				return generatedString

		nextSyms = followsPOS[curSym]
		chanceSym = random.randrange(10)
		if (chanceSym >= chanceNextFirst or len(nextSyms) < 6):
			curSym = nextSyms[0][0]
		elif (chanceSym >= chanceNext2t5):
			curSym = nextSyms[random.randrange(1,5)][0]
		else:
			curSym = nextSyms[random.randrange(5, len(nextSyms))][0]
	"""


	return generatedString


print(genTweet())