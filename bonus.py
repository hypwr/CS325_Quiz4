from ArrayChecker import arrayCheck as AC
from CreateRandom import randomArray as RA
from Counter import characterCounter as CC

#this is the same as question 8, just a different output
#if you want to test your own array, just us CC.countCharacters(yourValidArrayHere), or change the randomData variable to your own array.

randomData=RA.generateRandomArray()
if(AC.checkArray(randomData)==0):
    print("Input: "+str(randomData))
    countedData=CC.countCharacters(randomData)
    print("Output: "+str(countedData))
else:
    "Invalid array. Must of type int or str, and be a python list"