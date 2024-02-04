import array

def countCharacters(data):
    outputData=[]
    for i in data:
        x=len(str(i))
        outputData.append(x)
    return outputData
        