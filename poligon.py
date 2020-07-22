#E-közmű poligon2coordlist script

#import regex
import re

#import coordinate txt file
koordList = [line.rstrip('\n') for line in open("poli.txt")]

#simple replace
koordList = [line.replace('  0', '') for line in koordList]
koordList = [line.replace('  ', ' ') for line in koordList]
#regex replace
koordList = [re.sub('^[0-9]{1}\s', '', line) for line in koordList]
koordList = [re.sub('^[0-9]{2}\s', '', line) for line in koordList]

#Print data to console (only for testing)
#for line in koordList:
#    print (line)

#Count the lines in list
listLen = len(koordList)
#Def. a couter
num = 0

#open the input file in write mode
coords = open("poli.txt", "wt")

#overrite the input file with the resulting data
while num < listLen:
    coords.write(koordList[num] + "\n")
    num = num+1
    
#close the file
coords.close()



