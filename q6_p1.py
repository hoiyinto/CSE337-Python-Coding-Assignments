
thirdpower=lambda a : a*a*a

numberList=[]

for i in range(100, 1000):
	numberList.append(int(i))

def nar(x):
	sep=list(str(x))
	total=0
	for n in sep:
		total+=thirdpower(int(n))
	if total==x:
		return True
	else:
		return False		

narList = list(filter(nar,numberList))

print(narList)