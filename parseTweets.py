#Written by Lake
#help from http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#	for parsing
#used https://www.allmytweets.net, to access tweets

numsAndOpen = ["1","2","3","4","5","6","7","8","9","<"]

def parseTweets (txt_name, output_name):
	tweet_output = open(output_name, "w")
	txt_file = open(txt_name, "r")
	for line in txt_file:
		if (line[0:10] == '      <td>' and line[10] not in numsAndOpen and line[11] not in numsAndOpen):
			parsed_line = line[10:-6]
			parsed_line = trimLinks(parsed_line)
			parsed_line = trimLinks(parsed_line)
			print parsed_line
			tweet_output.write(parsed_line)
			tweet_output.write("\n")
			tweet_output.write("\n")

def trimLinks (line):
	if (line[-1:] == ">"):
		print "hello---------------------------------------------------"
		do_loop = True
		if (line[-4:] == "<br>"):
			do_loop = False
		line = line[:-4]
		if (do_loop):
			while (line[-1:] != "<"):
				line = line[:-1]
		line = line[:-2]
	return line

parseTweets("realDonaldTrumpunParsed","output.txt")