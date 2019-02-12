import time
import datetime

def q1p1():
	file=open('prices_sample.csv')

	filelist=[]

	for eachline in file:
		ele=eachline.split(',')
		dt = datetime.datetime.fromtimestamp(int(ele[0]))
		price= int(ele[1])
		dt_price_tuple=(dt,price);
		if len(filelist)==0:
			daylist=[dt_price_tuple]
			filelist.append(daylist)
		else:
			daylist=filelist[len(filelist)-1]
			year1=((daylist[0])[0]).year
			month1=((daylist[0])[0]).month
			day1=((daylist[0])[0]).day
			if year1==dt.year and month1==dt.month and day1==dt.day:
				daylist.append(dt_price_tuple)		
			else:
					daylist=[dt_price_tuple]
					filelist.append(daylist)	

	file.close()
	
	return filelist


filelist=q1p1()
outputfile=open("q1_p1_output.txt","w")
for day in filelist:
	outputfile.write((day[0])[0].strftime("%Y-%m-%d")+': ')
	for tuples in day:
		outputfile.write(str(tuples[1])+',')
	outputfile.write('\n')	
outputfile.close()