#REPRESENTING SIMPLE STRINGS
#Each charchter is represented by a number between 0 and 256 stored if __name__ == '__main__':
#8 bits of memory.
#We refer to '8 bits of memory as a "byte"'
#ord() tells us the numeric value of a simple ASCII charachter
print(ord('H')) #gives - 72
print(ord('e')) #gives - 101
print(ord('\n')) #gives - 10

while True:
    data = mysock.recv(512) #data is BYTES
    if (len(data) < 1):
        break
    mystring = print(data.decode()) #mystring is UNICODE
print(mystring)
