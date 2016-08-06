#!/usr/bin/env python

from bs4 import BeautifulSoup as HTMLparser
import requests
import time
import MySQLdb
def scanWebForElectionData():
	invalidStateNumbers=[]
	listOfElectionYears=[2000,2004,2008,2012]
	for year in listOfElectionYears:
		for numberCorrespondingToState in range(1,100):
			try:
				time.sleep(5)
				HTMLrequest=requests.get('http://uselectionatlas.org/RESULTS/datagraph.php?fips='+str(numberCorrespondingToState)+'&year='+str(year))
				parsedHTML=HTMLparser(HTMLrequest._content,"html.parser")
				parsedHTMLwithStateName=parsedHTML.find("div",class_="header")
				stateName=parsedHTMLwithStateName.contents[0].split(' ')[7]
				messyListOfInfo=parsedHTML.find("div",class_="info").find_all("table")
				for i in range(0,len(messyListOfInfo)):
					countyName=messyListOfInfo[i].tr.td.b.contents[0]
					messyListOfCandidates=messyListOfInfo[i].find_all("tr")
					for j in range(0,len(messyListOfCandidates)):
						if j==0:
							candidateName=messyListOfInfo[i].find_all("tr")[j].find_all("td")[1].contents[0]
							votePercentage=messyListOfInfo[i].find_all("tr")[j].find_all("td")[2].contents[0]
							voteTotal=messyListOfInfo[i].find_all("tr")[j].find_all("td")[3].contents[0]
						else:
							candidateName=messyListOfInfo[i].find_all("tr")[j].find_all("td")[0].contents[0]
							votePercentage=messyListOfInfo[i].find_all("tr")[j].find_all("td")[1].contents[0]
							voteTotal=messyListOfInfo[i].find_all("tr")[j].find_all("td")[2].contents[0]
						print str(year) + "\t" + stateName + " " + str(numberCorrespondingToState) + "\t" + countyName + "\t" + candidateName + "\t" + votePercentage + "\t" + voteTotal
					print "\n"
				print "\n\n"
			except AttributeError:
				print "State number " + str(numberCorrespondingToState) + " is invalid"
				invalidStateNumbers.append(numberCorrespondingToState)

if __name__ == "__main__":
	scanWebForElectionData()

