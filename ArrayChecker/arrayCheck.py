
def checkArray(data) -> int:
    #check for python list/array
    if(not isinstance(data,list)):
        return 1

    #check for int/str in data
    for i in data:
        if(isinstance(i,str) or isinstance(i,int)):
            continue
        else:
            return 1
    
    return 0
    