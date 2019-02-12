from q1_p1 import q1p1
import statistics 
import math

filelist=q1p1()

prices=[]

for day in filelist:
	for tuples in day:
		prices.append(tuples[1])

prices.sort()
p25th=int((prices[int(len(prices)*0.25)]+prices[int((len(prices)*0.25)-1)])/2)
p50th=int((prices[int(len(prices)*0.5)]+prices[int((len(prices)*0.5)-1)])/2)
p75th=int((prices[int(len(prices)*0.75)]+prices[int((len(prices)*0.75)-1)])/2)

meanOfdata=statistics.mean(prices) 

farthest=[]

for day in filelist:
	diff=0
	far=0
	for tuples in day:
		date=tuples[0]
		if math.fabs(tuples[1]-meanOfdata)>diff:
			far=tuples[1]
			diff=math.fabs(tuples[1]-meanOfdata)
	farthest.append((date,far,diff))

def getDiff(x):
	return x[2]

farthest.sort(reverse=True, key=getDiff)	

print('Five days with farthest price to the mean')
for n in range(5):
	print(((farthest[n])[0]).strftime("%Y-%m-%d")+' : '+str((farthest[n])[1]))

print("The 25th percentile : "+str(p25th))
print("The 50th percentile : "+str(p50th))
print("The 75th percentile : "+str(p75th))
print("Variance : % s" %(statistics.variance(prices,meanOfdata)))
