#a language of 'marker charachters'- programming with charachters

import re

#using re.search() like find()
handle = open('mbox-short.txt')
for line in handle:
    line = line.rstrip()
    if re.search('^From', line):
        print(line)
