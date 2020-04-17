#! c:\Python3\python.exe

#import tools
from bs4 import BeautifulSoup
import requests
import urllib
import argparse

def releasedate(rows, Month, Day, Year):
	versions = []
	counter = 0
	counter2 = 0
	for row in rows:
		if (str(row) == '<span class="release-date">', Month,' ', Day, '. ', Year, '</span>'):
			print(rows)
			# versions.append(str(rows[counter]))
			# counter2 = counter2 + 1
			# print(versions)
			# # print(x)
			# if (str(rows[counter + 1]) == '<span class="release-download"><a href="/downloads/release/python-274/"><span aria-hidden="true" class="icon-download"></span> Download</a></span>'):
				# #if link is found, go to download page
				# for link in rows[counter + 1].find_all('a'):
					# downloadurl = link.get('href')
					# downloadpage = requests.get('https://www.python.org' + downloadurl)
					# downloadsoup = BeautifulSoup(downloadpage.text, 'html.parser')
					# return downloadsoup
		counter = counter + 1
		
def downloadpage(downloadsoup):
	downloadlinks = downloadsoup.find_all('td')
	counter = 0
	for downloadlink in downloadlinks:
		if (downloadlink.text == 'Windows x86-64 MSI installer'):
			for download in downloadlinks[counter].find_all('a'):
				downloads = download.get('href')
				print("Downloading...")
				urllib.request.urlretrieve(downloads, "MasonMorris-Python-2-7-4.msi")
				print("File downloaded.")
		counter = counter + 1

def Main():
	parser = argparse.ArgumentParser()
	parser.add_argument("month", help = "Jan., Feb., March, April, May, June, July, Aug., Sept., Oct., Nov., Dec.", type = str, default = True)
	parser.add_argument("day", help = "day of the month", type = int, default = True)
	parser.add_argument("year", help = "full year, xxxx", type = int, default = True)
	args = parser.parse_args()
	
	Month = (args.month)
	Day = (args.day)
	Year = (args.year)
	
	#print(Month, Day, Year)
	
	url = 'https://python.org/downloads'
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	rows = soup.find_all('span')
	
	downloadsoup = releasedate(rows, Month, Day, Year)
	#downloadpage(downloadsoup)
Main()