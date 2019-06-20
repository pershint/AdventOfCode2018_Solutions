import numpy as np
import scipy as sp
import json
import re

if __name__=='__main__':
    filelines = []
    with open("./Day2Input.txt","r") as f:
        filelines = f.readlines()
    #We need to see for each line if:
    #  - It has two of any letter
    #  - If it has three of any letter
    #  BUT, if a letter appears three times, it won't count for both counts.
    threecounts = 0
    twocounts = 0
    #Let's do some regex expressions for fun
    for line in filelines:
        hasthree = False
        hastwo = False
        lineentries = set(list(line))
        for e in lineentries:
            if hasthree and hastwo:
                break
            elif line.count(e) == 3 and not hasthree:
                threecounts += 1
                hasthree = True
            elif line.count(e) == 2 and not hastwo:
                twocounts += 1
                hastwo = True
    print("OUR FINAL HASH IS: %i"%(twocounts*threecounts))
                 
