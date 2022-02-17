#!/usr/bin/env python3

#Russell / File Data Interactions

#1
with open("/etc/passwd","r") as hFile:
    strfiletext = hFile.read()
print(len(strfiletext))
print("The len() function is counting the amount of characters that are in the file")

#2
with open("/etc/passwd","r") as hFile:
    listfiletext = hFile.readlines()
print (len(listfiletext))
print("Function len() Is used to count the amount of lines in a file")

#3
with open("/etc/passwd","r") as hFile:
    countLines = 0
    try:
        while True:
            countLines += len(next(hFile))
    except StopIteration:
        print("Reached The End Of The File")
print(f"The length of /etc/passwd  is: {countLines}")
