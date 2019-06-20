import numpy

if __name__=="__main__":
    #Load input file
    alldata = []
    with open("Day1Input.txt","r") as f:
        i = 0
        for line in f:
            num = int(line)
            i+=num
    print("SUM OF ALL INPUTS IS: %i"%(i))
