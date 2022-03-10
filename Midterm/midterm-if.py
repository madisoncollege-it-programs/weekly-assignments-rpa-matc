#!/usr/bin/env python3
print("Name: Russell Pa")
#Midterm Project IF
Counter = -1
Total = 0
with open("Midterm-if.txt","r") as hfile:
    for line in hfile:
        Counter += 1
        if "gmeach18@ed.gov" in line:
            print (f"{Counter} gmeach18@ed.gov")
            Total += Counter
        elif "248.253.63.149" in line:
            print (f"{Counter} 248.253.63.149")
            Total += Counter
        elif "Whiteland" in line:
            print (f"{Counter} Whiteland")
            Total += Counter
        elif "80.222.19.190" in line:
            print (f"{Counter} 80.222.19.190")
            Total += Counter
        elif "Kayley" in line:
            print (f"{Counter} Kayley")
            Total += Counter
        elif "dcassyqw@microsoft.com" in line:
            print (f"{Counter} dcassyqw@microsoft.com")
            Total += Counter
print(f"The total is: {Total}")
