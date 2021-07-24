#a language of 'marker charachters'- programming with charachters

import re

#using re.search() like find()
handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if re.search('^From', line):
        print(line)

#WILDCARD CHARACHTERS

#'^' matches the start of the line
#'.' matches any charachter
#if you add '*', the charachter is 'any number of times'

^X.*:

#'\S' matches any non-whitespace charachter
#'+' means one or more times

^X-\S+:

#using re.findall() extracts strings which are matching

[0-9]+

import re
x = 'My 2 favorite numbers are 19 and 42.'
y = re.findall('[0-9]+', x)
print(y) #gives - ['2', '19', '42']

y = re.findall('[AEIOU]'+, x)
print(y) #gives - []

#GREEDY MATCHING
#'*' and '+' push OUTWARD in both directions(greedy) to match the largest
#possible string

import re
x = 'From: Using the : charachter'
y = re.findall('^F.+', x)
print(y) #gives - ['From: Using the :']

#NON-GREEDY MATCHING
#'?' means one or more charachters but are not greedy

import re
x = 'From: Using the : charachter'
y = re.findall('^F.+?', x)
print(y) #gives - ['From:']

import re

x = 'From stephen.mandall@uct.ac.ze Sat Jan 5 09:14:16 2008'
y = re.findall('^ From.(\S+@\S+)', x)
#'\S+@\S+' gives at least one non-whitespace charachter
#'()' are not part of the match - but they tell where to START and STOP
#what string to extract
print(y) #gives - ['stephen.mandall@uct.ac.ze']

import re
x = 'From stephen.mandall@uct.ac.ze Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)', x)
#'[^ ]' - matches non-blank charachter (non-blank means everything but a space)
print(y) #gives - ['uct.ac.ze']

#Spam Confidence

import re
handle = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    line = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1 :
        continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))

#ESCAPE CHARACHTER
#If you want a special regular expression charachter to just behave
#normally (most of the time) you prefix it with '\'

import re
x = 'We just recieved $10.00 for cookies'
y = re.findall('\$[0-9.]+', x)
#'\$[0-9.]+' - \$ gives real dollar sign, '.' means a digit or period
print(y) #gives - ['$10.00']
