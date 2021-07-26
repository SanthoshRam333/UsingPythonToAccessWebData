#In this assignment you will write a Python program somewhat similar to
#http://www.py4e.com/code3/geoxml.py. The program will prompt for a URL,
#read the XML data from that URL using urllib and then parse and extract
#the comment counts from the XML data, compute the sum of the numbers
#in the file.

import urllib.request as ur
import xml.etree.ElementTree as et

url = input('Enter location: ')
# http://python-data.dr-chuck.net/comments_42.xml


total_number = 0
sum = 0

print('Retrieving', url)
xml = ur.urlopen(url).read()
print('Retrieved', len(xml), 'characters')

tree = et.fromstring(xml)
counts = tree.findall('.//count')
for count in counts:
    sum += int(count.text)
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)
