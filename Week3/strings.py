#!/usr/bin/env python3

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.45166295

print (f"Hello {varName: <0s}")

print (f"{varRed: <0s}-{varGreen: <0s}-{varBlue: <0s}")

print (f"Is this {varGreen.lower(): <0s} or {varBlue.lower(): <0s}?")

print (f"My name is {varName.upper()}")

print (f"[{varRed:$^10s}] [{varGreen:$^10s}] [{varBlue:$^10s}]")

print (f"First Color:[{varRed: <0s}] Second Color:[{varGreen: <0s}] Third Color:[{varBlue: <0s}]")

print (f"{varBlue * 10}")

print (f"[{varRed:+^7s}]")

print (f"[{varGreen.lower():=<7s}]")

print (f"[{varBlue.lower():*>9s}]")

print (f"[{varRed[::-1]}][{varGreen}][{varBlue[::-1]}]")

print (f"I have ${varLoot: .2f}")

print (f"{varLoot}")

print (f"{varLoot:.1f}")
