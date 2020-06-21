import random

def file_lengthy(fname):
    with open(fname) as f:
            for i in enumerate(f):
                    pass
    return i + 1


def getQuoteOfDay(fname):
    tempVar = ''
    with open(fname, mode="r") as f:
        fs = f.readlines()
        #print(fs[random.randint(1,len(fs) -1)])
        tempVar = fs[random.randint(1,len(fs) -1)]
    return tempVar   

#fname = "quotes.txt"
#getQuoteOfDay(fname)
