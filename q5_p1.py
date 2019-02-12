import re
def frequency(lst):
	counts = {}
	for ele in lst:
		counts[ele] = counts.get(ele,0) + 1
	return counts

def isPalindrome(str): 
	n=len(str)/2
	if len(str)%2!=0:
		n=(len(str)-1)/2
	for i in range(int(n)):
		if str[i] != str[len(str)-i-1]: 
			return False
	return True		

def validPassword(username,pwd):
	if len(pwd)<6 or len(pwd)>20: #length
		return False
	if bool(re.search(r'\d', pwd))==False: #numerical character
		return False
	if bool(re.search(r"[A-Z]+",pwd))==False: #upper-case character
		return False
	
	regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') #special character
	if regex.search(pwd) == None:
		return False
	
	listOfsubstrings=[] 	#substring
	for x in range(len(pwd)-2):
		subs=pwd[x]+pwd[x+1]+pwd[x+2]
		listOfsubstrings.append(subs)
	counts=frequency(listOfsubstrings)	
	finalcounts={k : v for k,v in counts.items() if v > 1}
	if len(finalcounts)>0:
		return False

	if isPalindrome(pwd):	#palindrome
		return False
	
	counts2=frequency(list(pwd)) #number of unique characters
	if len(counts2)<(len(pwd)/2):
		return False 

	if username in pwd: #Username
		return False

	if username[::-1] in pwd: #reverse
		return False
	
	return True	

validPassword('user1','abAa5b&cabc')