def count(lst):
	tupleList=list(map(lambda x:[x,int(1)],lst))

	for i in range(0,len(tupleList)-1):
		str=(tupleList[i])[0]
		for n in range(i+1,len(tupleList)):
			if (tupleList[n])[0]==str:
				(tupleList[i])[1]+=((tupleList[n])[1])
				(tupleList[n])[1]=int(0)			

	output=list(filter(lambda x:x[1]>0,tupleList))

	finaloutput=list(map(lambda x:(x[0],x[1]),output))

	print(finaloutput)

count(['abc','sdf','abc','888','90w3','90w3','sdf'])