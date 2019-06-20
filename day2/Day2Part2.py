import numpy as np
import scipy as sp
import json
import re

def rebuildstring(stringlist):
    #This is quite inefficient, but let's do it
    builtstring = ''
    for entry in stringlist:
        builtstring = builtstring + entry
    return builtstring

if __name__=='__main__':
    filelines = []
    with open("./Day2Input.txt","r") as f:
        filelines = f.readlines()
    #Now, we need to find two lines that differ by exactly one character in one spot
    therightline = "NONE"
    for j,aline in enumerate(filelines):
        if j==0:
            continue
        #Compare the jth line with all prev. lines
        for k in range(j):
            #Turn our strings to lists with a letter in each entry
            thisline = list(filelines[j])
            prevline = list(filelines[k])
            numdiffs = 0
            diffinds = []
            #Abusing the fact that the lines are all equal length
            for i,value in enumerate(thisline):
                if thisline[i] != prevline[i]:
                    numdiffs+=1
                    diffinds.append(i)
            if numdiffs == 1:
                result = ("FOUND OUR LINES DIFFERING BY ONE." +
                        "AT LINES %i and %i"%(j,k) + 
                        "AND REMOVED INDEX IS %i"%(i))
                print(result)
                #Remove the different element, rebuild the string and break
                therightlineelements = thisline
                del(therightlineelements[diffinds[0]])
                therightline = rebuildstring(therightlineelements)
                break
    print("THE SOLUTION LINE IS %s"%(therightline))

