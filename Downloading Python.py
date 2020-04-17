#! c:\Python3\python.exe

#import tools
from bs4 import BeautifulSoup
import requests
import urllib

#get HTML from website
url = 'https://python.org/downloads'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

#find needed rows
rows = soup.find_all('span')

#find download link based on release date
counter = 0
for row in rows:
	if (str(row) == '<span class="release-date">April 6, 2013</span>'):
		if (str(rows[counter + 1]) == '<span class="release-download"><a href="/downloads/release/python-274/"><span aria-hidden="true" class="icon-download"></span> Download</a></span>'):
            #if link is found, go to download page
			for link in rows[counter + 1].find_all('a'):
				downloadurl = link.get('href')
				downloadpage = requests.get('https://www.python.org' + downloadurl)
				downloadsoup = BeautifulSoup(downloadpage.text, 'html.parser')
	counter = counter + 1

#finds the windows installer and downloads file
downloadlinks = downloadsoup.find_all('td')
counter2 = 0
for downloadlink in downloadlinks:
    if (downloadlink.text == 'Windows x86-64 MSI installer'):
        for download in downloadlinks[counter2].find_all('a'):
            downloads = download.get('href')
            print("Downloading...")
            urllib.request.urlretrieve(downloads, "MasonMorris-Python-2-7-4.msi")
            print("File downloaded.")
    counter2 = counter2 + 1