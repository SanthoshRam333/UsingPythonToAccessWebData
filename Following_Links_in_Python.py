#In this assignment you will write a Python program that expands on
#http://www.py4e.com/code3/urllinks.py. The program will use urllib to
# read the HTML from the data files below, extract the href= vaues
#from the anchor tags, scan for a tag that is in a particular position
#relative to the first name in the list, follow that link and repeat
#the process a number of times and report the last name you find.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#SSL Certification Error Handle
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Data Collection
link = input('Enter URL: ')
cont = int(input('Enter count: '))
line = int(input('Enter position: '))

print('Retrieving: %s' % link)
for i in range(0, cont):
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    cn = 0
    ps = 0
    for tag in tags:
        ps += 1
        if ps == line:
            print('Retrieving: %s' % str(tag.get('href', None)))
            link = str(tag.get('href', None))
            ps = 0
            break
