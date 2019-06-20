import numpy as np

if __name__=="__main__":
    #Load input file
    alldata = []
    with open("Day1Input.txt","r") as f:
        for line in f:
            alldata.append(line)
    #Add values in the dataset until you find a duplicate; 
    #loop to start if you reach end of list
    haveseens = np.array([])
    summedvalue = 0
    foundduplicate = False 
    while not foundduplicate:
        print("BEGINNING OF LOOP")
        for i in alldata:
            summedvalue = summedvalue + int(i)
            if len(np.where(haveseens==summedvalue)[0]) == 0:
                np.append(haveseens,summedvalue)
            else:
                foundduplicate = True 
                break
            print("SUMMEDVALUEIS: %s"%(summedvalue))
    print("FOUND THE DUPLICATE NUM: %s"%(summedvalue))

