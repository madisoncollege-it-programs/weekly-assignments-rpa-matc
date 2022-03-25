#!/usr/bin/env python3


def degrees_f2c():
    f = int(input("Enter your temperature in fahrenheit: "))
    c = (f-32) * 5.0/9.0
    print ("Your temperature is: ",c, "in celcius")
degrees_f2c()
