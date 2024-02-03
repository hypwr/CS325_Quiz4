class rectangle:
    def __init__(self, length, width) -> None:
        self._length = length
        self._width = width

    @property
    def rectangleProp(self):
        return self._length, self._width
    
    @rectangleProp.setter
    def rectangleProp(self, new_prop):
        if not isinstance(new_prop, int):
            num1 , num2 = new_prop
        else:
            num1=new_prop
            num2="no info given"
        self._length=num1
        self._width=num2

def main()->None:
    r1 = rectangle(6,5)
    print("Rectangular Dimensions: "+str(r1.rectangleProp))

    r1.rectangleProp = 3
    print("Rectangular Dimensions: "+str(r1.rectangleProp))

    r1.rectangleProp = [10,2]
    print("Rectangular Dimensions: "+str(r1.rectangleProp))



main()


