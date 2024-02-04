class rectangle:
    def __init__(self, length, width) -> None:
        self._length = length
        self._width = width

    def rectLengGet(self):
        return self._length
    
    def rectWidthGet(self):
        return self._width

    def rectPropGet(self):
        return self._length, self._width
    
    def rectLengSet(self, length):
        self._length=length

    def rectWidthSet(self, width):
        self._width=width
    
    def rectPropSet(self, length, width):
        self._length=length
        self._width=width

def main()->None:
    r1 = rectangle(6,5)
    print("Rectangular Dimensions: "+str(r1.rectPropGet()))

    r1.rectPropSet(3,0)
    print("Rectangular Dimensions: "+str(r1.rectPropGet()))

    r1.rectWidthSet(15)
    print("Rectangular Dimensions: "+str(r1.rectPropGet()))

    r1.rectPropSet(10,2)
    print("Rectangular Dimensions: "+str(r1.rectPropGet()))

    print("It could also be written as: "+str(r1.rectLengGet())+" x "+str(r1.rectWidthGet()))

main()


