from bs4 import BeautifulSoup as bs
import requests
import time
import MySQLdb
def scan():
	invalid_numbers=[]
	for year in [2000,2004,2008,2012]:
		for state_number in range(1,100):
			try:
				time.sleep(5)
				r=requests.get('http://uselectionatlas.org/RESULTS/datagraph.php?fips='+str(state_number)+'&year='+str(year))
				soup=bs(r._content,"html.parser")
				q=soup.find("div",class_="header")
				state=q.contents[0].split(' ')[7]
		
				w=soup.find("div",class_="info").find_all("table")
				for i in range(0,len(w)):
					county=w[i].tr.td.b.contents[0]
					q=w[i].find_all("tr")
					for j in range(0,len(q)):
						if j==0:
							candidate=w[i].find_all("tr")[j].find_all("td")[1].contents[0]
							vote_perc=w[i].find_all("tr")[j].find_all("td")[2].contents[0]
							vote_total=w[i].find_all("tr")[j].find_all("td")[3].contents[0]
						else:
							candidate=w[i].find_all("tr")[j].find_all("td")[0].contents[0]
							vote_perc=w[i].find_all("tr")[j].find_all("td")[1].contents[0]
							vote_total=w[i].find_all("tr")[j].find_all("td")[2].contents[0]
						print str(year) + "\t" + state + " " + str(state_number) + "\t" + county + "\t" + candidate + "\t" + vote_perc + "\t" + vote_total
					print "\n"
				print "\n\n"
			except AttributeError:
				print "State number " + str(state_number) + " is invalid"
				invalid_numbers.append(state_number)


