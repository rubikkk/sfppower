import time
import string

filenameIn = "power-" + time.strftime("%Y-%m-%d")
filenameOut = "/home/dcastro/pexpect/sfppower/data/Clean-power-" + time.strftime("%Y-%m-%d")
#date=raw_input("nom data: ")

ip=""
power=""
mid=[]

fileIn = open(filenameIn, 'r')
fileOut = open(filenameOut, 'w')

for line in fileIn:
        if '10.167' in line:
                ip=line
        if 'Gi0/' in line:#en el cas dels 3402
                power=line
                mid = power.split('    ')[4]
                out=ip + ''.join(mid)
                fileOut.write(out + "\n")
