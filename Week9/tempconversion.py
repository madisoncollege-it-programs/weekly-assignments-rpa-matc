#!/usr/bin/env python3


print ("""Please choose between fahrenheit or celcius.
1 for fahrenheit, 2 for celcius.""")

a = input("->")

if a == "1":
    import f2c
else:
    import c2f
