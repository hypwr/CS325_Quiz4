from ArrayChecker import arrayCheck as AC
from CreateRandom import randomArray as RA
from Counter import characterCounter as CC

randomData=RA.generateRandomArray()
if(AC.checkArray(randomData)==0):
    print("Starting array: "+str(randomData))
    countedData=CC.countCharacters(randomData)
    print("Counted array: "+str(countedData))
else:
    "Invalid array. Must of type int or str, and be a python list"
    

