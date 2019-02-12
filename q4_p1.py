def dictionary():
	def frequency(lst):
		counts = {}
		for ele in lst:
			counts[ele] = counts.get(ele,0) + 1
		return counts

	filename=input("Please enter a filename: ")
	n=input("Please enter a number: ")	

	inputfile=open(str(filename),"r")
	wholeFile=inputfile.read()
	allwords=wholeFile.split()

	nGramWordList=[]
	for pos in range(len(allwords)-int(n)+1): 
		nGramWord=''
		for a in range(int(n)):
			nGramWord+=allwords[pos+a]
			nGramWord+=' '
		nGramWordList.append(nGramWord[:len(nGramWord)-1])

	output=frequency(nGramWordList)
	inputfile.close()

	return output


def dictWithoutOnes():
	output=dictionary()
	finaloutput={k : v for k,v in output.items() if v > 1}
	return finaloutput	

print(dictWithoutOnes())



