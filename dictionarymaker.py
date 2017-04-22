def POSfreq(taggedwords): #list of lists
	# tagged words should be in the form of a list of lists of tuples
	d = {}
	for lst in taggedwords:
                for l in lst:
                        word = l[0]
                        tag = l[1]
                        if tag in d:
                                wlist = [x[0] for x in d[tag]]
                                if word in wlist:
                                        for pair in d[tag]:
                                                if pair[0] == word:
                                                        pair[1] += 1
                                else:
                                        d[tag] += [[word, 1]]
                        else:
                                d[tag] = [[word, 1]]
        return d
