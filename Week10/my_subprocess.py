#!/usr/bin/env python3
#Script of using a subprocess
import subprocess

myProc = subprocess.run(['ps','-axco', 'command'],stdout=subprocess.PIPE)
#myProc = subprocess.Popen(['ls', '-la'], shell=True,stdout=subprocess.PIPE)
#print (f"myProc: {myProc}")
print (f"command line: {myProc.args}\n")
print (f"exit status: {myProc.returncode}\n")
lstdout = myProc.stdout.decode().split('\n')
#print (f"output of command: {lstdout}")
myProcString = myProc.stdout.decode()
myProcList = myProcString.split('\n')
len = -1
for line in myProcList:
    len += 1
    print (f"{line}\n")
    print (len)
