import math
def expo(lst):
	outputlist=list(map(lambda x:math.pow(2,x),lst))
	outputlist2=list(filter(lambda x:x<1000,outputlist))
	print(outputlist2)

expo([1,4,5,6,7,11,10,20])