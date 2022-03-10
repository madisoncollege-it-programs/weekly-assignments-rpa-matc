#!/usr/bin/env python3
print ("Name: Russell Pa")
#Midterm project slicing

with open ("slicing-file.txt","r") as hFile:
    list = hFile.readlines()

a = (f"{list[-3:-2:]}")
#print (a)
b = (f"{list[2:5:1]}")
#print (b)
c = (f"{list[-10:-16:-2]}")
#print (c)
d = (f"{list[10:13:1]}")
#print (d)
e = (f"{list[8:5:-1]}")
#print (e)

quote = (a,b,c,d,e)

print(quote)
