#The basic outline of this problem is to read the file, look for
#integers using the re.findall(), looking for a regular expression of
#'[0-9]+' and then converting the extracted strings to integers and
# summing up the integers.
import re
handle = open('regex_sum_1200111.txt')
numlist = list()
for line in handle:
    line = line.rstrip()
    line = re.findall('[0-9]+', line)
    if len(line) < 1 :
        continue
    for i in range(len(line)):
        num = float(line[i])
        numlist.append(num)
print('Sum:',sum(numlist))
