#!/usr/bin/env python3

#Russell Pa / Dictionaries.py (Script about using a dictionary and different commands involving the dictionary)

MyDict = {"Server1.testlab.com":"192.168.1.10","Server2.testlab.com":"192.168.1.11","Server3.testlab.com":"192.168.1.12","Server4.testlab.com":"192.168.1.13","Server5.testlab.com":"192.168.1.14","Server6.testlab.com":"192.168.1.15"}
print (MyDict.keys())
print (MyDict.values())
print (MyDict.items())
MyDict = {"Server1.testlab.com":"192.168.1.10","Server2.testlab.com":"192.168.1.11","Server3.testlab.com":"192.168.1.12","Server4.testlab.com":"192.168.1.13","Server5.testlab.com":"192.168.1.14","Server6.testlab.com":"192.168.1.15","Server7.testlab.com":"192.168.1.16","Server8.testlab.com":"192.168.1.17"}
print ("Server2.testlab.com" in MyDict)
print ("Server10.testlab.com" in MyDict)
