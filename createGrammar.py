# Name: Solomon Lake Giffen-Hunter

terminals = set(['that','this','a','book','flight','meal','money','include','prefer','I','she','me','Houston','TWA','does','from','to','on','near','through'])

nonterminals = set(['S','NP','Nominal','VP','PP','Det','Noun','Verb','Pronoun','Proper-Noun','Aux','Preposition'])

grammar = {'S':[['NP','VP'],['Aux','NP','VP'],['VP']],'NP':[['Pronoun'],['Proper-Noun'],['Det','Nominal']],'Nominal':[['Noun'],['Nominal','Noun'],['Nominal','PP']],'VP':[['Verb'],['Verb','NP'],['Verb','NP','PP'],['Verb','PP'],['VP','PP']],'PP':[['Preposition','NP']],'Det':[['that','this','a']],'Noun':[['book','flight','meal','money']],'Verb':[['book','include','prefer']],'Pronoun':[['I','she','me']],'Proper-Noun':[['Houston','TWA']],'Aux':[['does']],'Preposition':[['from','to','on','near','through']]}

# This function determines whether a grammar is in Chomsky Normal Form

# TODO: Add to set of nonterminals when creating in grammar

# I turned these into functions so they can be used in their components later to
#	streamline the grammar conversion
def InCNF(g):
	inCNF = True
	for left in g:
		inCNF = inCNF and RightSideCNF(g[left])
	return inCNF

def RightSideCNF(rightSide):
	rsCNF = True
	for right in rightSide:
		rsCNF = rsCNF and RightCNF(right)
	return rsCNF

def RightCNF(right):
	verboseR = False
	if (len(right) == 2):
			if (right[0] not in nonterminals or right[1] not in nonterminals):
				if (verboseR):
					print(right)
				return False
	elif (len(right) == 1):
		if (right[0] not in terminals):
			if (verboseR):
				print(right)
			return False
	else:
		if (verboseR):
			print(right)
		return False
	return True

					
# This function takes a grammar and returns an equivalent grammar in Chomsky Normal Form
"""
1. if right is single nonterminal, then take nonterminal's list and add it to nonTerm
		then loop through that list again
2. if right is > 1 and all are terminals, then give each terminal its own list
3. if right is 2 and there is one terminal and one nonterminal, then create new nonterminal
	in the place of the terminal, and set the terminal as a right of the new nonterminal
4. if right is > 2 (and not all nonterminals), then create new nonterminal in the place
	of every term after the first term, then put all of those terms as a right of the new
	nonterminal, then loop through list again
"""
def ConvertToCNF(g):
	newG = {}
	newNTCounter = 0
	for left in g:
		#print(left)
		if (RightSideCNF(g[left])):
			newG[left] = g[left]
		else:
			rightSideCNFandNewNonTerms = ConvertRightSide(g[left], g, {}, newNTCounter)
			newG[left] = rightSideCNFandNewNonTerms[0]
			newG.update(rightSideCNFandNewNonTerms[1])
			newNTCounter = rightSideCNFandNewNonTerms[2]

	return newG

# This function takes the rightside, the grammar, an empty dictionary that will contain new grammar
#	items and a counter used for making new grammar pieces
# This function returns a new rightside and a dictionary of new grammar terms
def ConvertRightSide(rightSide, g, newNTs, nNTC):
	if (RightSideCNF(rightSide)):
		return [rightSide, newNTs, nNTC]

	newRightSide = []
	for right in rightSide:
		if (RightCNF(right)):
			newRightSide.append(right)

		elif (len(right) == 1):
			# case: single nonterminal
			#print("single nonterminal")
			if (right[0] in g):
				nonTermRS = g[right[0]]
			else:
				nonTermRS = newNTs[right[0]]
			restOfR = rightSide[rightSide.index(right)+1:]
			for r in restOfR:
				newRightSide.append(r)
			for nonTermRight in nonTermRS:
				newRightSide.append(nonTermRight)
			return ConvertRightSide(newRightSide, g, newNTs, nNTC)

		elif (len(right) > 1 and AllTerminals(right)):
			# this will make the grammar look nicer, reduce number of nonterminals
			for term in right:
				newRightSide.append([term])

		elif (len(right) == 2):
			# case: one terminal and one nonterminal
			if (right[0] in terminals):
				T = right[0]
				NT = right[1]
			else:
				T = right[1]
				NT = right[0]
			newNT = T + 'NT'
			nonterminals.add(newNT)
			if (newNT not in g and newNT not in newNTs):
				# a newNT hasn't already been created for this terminal
				newNTs[newNT] = [[T]]
			# ensures ordering stays the same
			if (right[0] in terminals):
				newRightSide.append([newNT, NT])
			else:
				newRightSide.append([NT, newNT])

		else:
			# case: more than 2 terms
			#print("more than 2 terms")
			newNT = right[0] + 'NT' + str(nNTC)
			nonterminals.add(newNT)
			#print(nNTC)
			nNTC += 1
			newRightSide.append([right[0], newNT])
			#print("more than 2 terms")
			rightSideANDnewNonTerms = ConvertRightSide([right[1:]], g, newNTs, nNTC)
			newNTs.update(rightSideANDnewNonTerms[1])
			newNTs[newNT] = rightSideANDnewNonTerms[0]
			nNTC = rightSideANDnewNonTerms[2]

	return [newRightSide, newNTs, nNTC]

# This function is a small helper function that checks if all the terms in a rightside are terminals
#	in which case it just makes them their own rightside term
def AllTerminals(right):
	for term in right:
		if (term not in terminals):
			return False
	return True
		
	

# This function takes a grammar and a string and returns True if that grammar generates that string, False otherwise. 

def CKYRecognizer(g,s):
	# for rsplit used: stackoverflow.com/questions/19303429/select-last-chars-of-string-until-whitespace-in-python
	sentence = s.rsplit(' ')
	# create matrix:
	matrix = []
	for i in range(0, len(sentence)):
		matrix.append([])
		for j in range (0, len(sentence)+1):
			matrix[i].append([])

	for j in range (1, len(sentence)+1):
		for left in g:
			if ([sentence[j-1]] in g[left]):
				matrix[j-1][j].append(left)

		#PrintMatrix(matrix)
		for i in range (j-2, -1, -1):
			for k in range (i+1, j):
				#loop through matrix lists
				for B in matrix[i][k]:
					for C in matrix[k][j]:
						for A in g:
							if ([B,C] in g[A]):
								matrix[i][j].append(A)

	#PrintMatrix(matrix) #can include this line to see the matrix
	return ('S' in matrix[0][len(sentence)])

def PrintMatrix(matrix):
	for i in matrix:
		print(i)



# Extra Credit (optional): Modify your CKYRecognizer function to instead return a valid parse of the string, if one exists.

def CKYParser(g,s):
	# for rsplit used: stackoverflow.com/questions/19303429/select-last-chars-of-string-until-whitespace-in-python
	sentence = s.rsplit(' ')
	# create matrix:
	matrix = []
	for i in range(0, len(sentence)):
		matrix.append([])
		for j in range (0, len(sentence)+1):
			matrix[i].append([])

	for j in range (1, len(sentence)+1):
		for left in g:
			if ([sentence[j-1]] in g[left]):
				matrix[j-1][j].append([left, sentence[j-1], "terminal"])

		for i in range (j-2, -1, -1):
			for k in range (i+1, j):
				#loop through matrix lists
				for B in matrix[i][k]:
					for C in matrix[k][j]:
						Bpos = matrix[i][k].index(B)
						Cpos = matrix[k][j].index(C)
						for A in g:
							if ([B[0],C[0]] in g[A]):
								matrix[i][j].append([A, [i,k,Bpos], [k,j,Cpos]])

	#PrintMatrix(matrix) #can include this line to see the matrix
	for right in matrix[0][len(sentence)]:
		if ('S' == right[0]):
			return CreateParse(matrix, sentence)
	else:
		print("error, not in grammar")
		return []

def CreateParse(matrix, s):
	parsedS = []
	for t in matrix[0][len(s)]:
		if (t[0] == 'S'):
			parsedS.append('S')
			if (len(s) < 2):
				parsedS.append(t[1])
			else:
				parsedS.append([CreatePRec(matrix[t[1][0]][t[1][1]][t[1][2]],matrix), CreatePRec(matrix[t[2][0]][t[2][1]][t[2][2]],matrix)])
			break

	return parsedS

# recursion, starting from S in the top right corner
def CreatePRec(t, m):
	#print(t)
	if (t[2] == "terminal"):
		return [t[0], t[1]]
	else:
		return [t[0], [CreatePRec(m[t[1][0]][t[1][1]][t[1][2]], m), CreatePRec(m[t[2][0]][t[2][1]][t[2][2]], m)]]



# Demonstrations
print ("Initial grammar in CNF?")
print (InCNF(grammar), "\n") # Should return False!

print("New grammar:")
newgrammar = ConvertToCNF(grammar)
print(newgrammar, "\n")

print ("New grammar in CNF?")
print (InCNF(newgrammar), "\n") # Should return True!

print ("book that flight through Houston: Recognized?")
print (CKYRecognizer(newgrammar,'book that flight through Houston'), "\n") # Should return True!



# Add more tests of CKYRecognizer here.
t0 = 'I prefer TWA to Houston'
t1 = 'I book a flight through Houston'
t2 = 'I include a book near Houston'
t3 = 'You rock'
t4 = 'Houston a prefer that this a flight I'
t5 = 'I prefer a meal near Houston'
t6 = 'book'
t7 = ''
t8 = 'book that meal'

#(['that','this','a','book','flight','meal','money','include','prefer','I','she','me',
	#'Houston','TWA','does','from','to','on','near','through'])

testList = [t0,t1,t2,t3,t4,t5,t6,t7,t8]

print("Running CKYRecognizer tests:")
for test in testList:
	print (test)
	print (CKYRecognizer(newgrammar, test), "\n")
	

# Extra Credit: Add tests of CKYParse here.

print("Running CKYParser tests:")
for test in testList:
	print (test)
	print (CKYParser(newgrammar, test), "\n")




