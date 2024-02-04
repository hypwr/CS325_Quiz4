import random
import array

def generateRandomArray():
    outputArray=[]
    selectionArray=[5,
                    44,
                    529,
                    2034,
                    90325,
                    304312,
                    13460987,
                    "a",
                    "be",
                    "thr",
                    "lock",
                    "first",
                    "combine",
                    "purple",
                    "15fifthteen"
                    ]
    #select array size between 1 and 5
    arraySize=random.randint(1,5)
    i=1
    while(i<=arraySize):
        outputArray.append(selectionArray[random.randint(0,14)])
        i+=1
    return outputArray
    

    
        