#!/usr/bin/env python3

# Step 1
varString = "Here is a nice string to slice"
varList = ["Here","is","a","nice","list","to","slice"]

# Step 2
print ({varString[3:30:1]})
print ({varString[0:3:1]})
print ({varString[3:12:1]})
print ({varString[0:30:2]})
print ({varString[::-1]})

# Step 3
print (varList[::-1])
print (varList[2::-1])
print (varList[2:4:1])
print (varList[0:7:3])
print (varList[1:7:1])

# Step 4
for X in varString: print(f"this is X: {X}")

# Step 5
for X in varList: print(f"This is X: {X}")

