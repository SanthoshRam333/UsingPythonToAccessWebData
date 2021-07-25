#WEB SCRAPPING
#pull data - particularly social data - who links to who?
#get your own data back out of some system that has no "export capability"
#monitor a site for new information
#spider the web to make a database for a search engine

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ') #Enter - http://www.dr-chuck.com/page1.html
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#Retrive all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None)) #prints - http://www.dr-chuck.com/page2.html
