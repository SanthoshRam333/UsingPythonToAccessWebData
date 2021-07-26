#In this assignment you will write a Python program somewhat similar to
#http://www.py4e.com/code3/json2.py. The program will prompt for a URL,
#read the JSON data from that URL using urllib and then parse and extract
# the comment counts from the JSON data, compute the sum of the numbers
#in the file and enter the sum below:

import urllib.request as ur
import json

# json_url = 'http://python-data.dr-chuck.net/comments_42.json'

json_url = input("Enter location: ")
print("Retrieving ", json_url)
data = ur.urlopen(json_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
json_obj = json.loads(data)

sum = 0
total_number = 0

for comment in json_obj["comments"]:
    sum += int(comment["count"])
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)
