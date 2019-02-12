import urllib.request
from bs4 import BeautifulSoup


def q3():
	response = urllib.request.urlopen("https://finance.yahoo.com/commodities")
	soup = BeautifulSoup(response.read(), "html.parser")

	symbol=soup.find_all("td",class_="data-col0 Ta(start) Pstart(6px)")
	name=soup.find_all("td",class_="data-col1 Ta(start) Pend(10px)")
	lastPrice=soup.find_all("td",class_="data-col2 Ta(end) Pstart(20px)")
	marketTime=soup.find_all("td",class_="data-col3 Ta(end) Pstart(20px)")

	commodities=[]
	com=[]

	for n in range(len(symbol)):
		com.append(symbol[n].getText())
		com.append(name[n].getText())
		com.append(lastPrice[n].getText())
		com.append(marketTime[n].getText())
		commodities.append(com)
		com=[]

	return commodities	


commodities=q3()
outputfile=open("commodities.txt","w")
for each in commodities:
	for field in each:
		outputfile.write(str(field)+',')
	outputfile.write('\n')		
outputfile.close()
