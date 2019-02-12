from q1_p1 import q1p1

filelist=q1p1()

weeklist=[]
week=[]
for day in filelist:
	if int(((day[0])[0]).strftime('%w'))<7:
		week.append(day)
	if int(((day[0])[0]).strftime('%w'))==0:
		weeklist.append(week)
		week=[]	
weeklist.append(week)						

def getP(x):
	return x[1]

outputfile=open("q2_output.txt","w")		

for week in weeklist:
	outputfile.write((((week[0])[0])[0]).strftime("%Y-%m-%d")+':')
	no=0
	total=0
	maxP=0
	minP=0
	for day in week:
		for prices in day:
			no+=1
			total+=prices[1]
		if maxP==0 and minP==0:
			maxP=(max(day,key=getP))[1]
			minP=(min(day,key=getP))[1]
		else:
			if (max(day,key=getP))[1]>maxP:
				maxP=(max(day,key=getP))[1]
			if (min(day,key=getP))[1]<minP:
				minP=(min(day,key=getP))[1]		
	outputfile.write(str(maxP)+','+str(minP)+','+str(total/no)+'\n')
		
outputfile.close()
