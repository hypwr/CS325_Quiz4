from abc import ABC, abstractmethod

class Creature(ABC):
    @abstractmethod
    def move(self,distance):
        pass

    @abstractmethod
    def eat(self,food):
        pass

class Human(Creature):
    def __init__(self,name) -> None:
        self.name=name
        self.position=0
        self.hp=10

    def move(self,distance):
        self.distance=distance
        if(distance<0):
            print(self.name,"walked",abs(distance),"ft down.")
            self.position=int(self.position)+int(distance)
        elif(distance>0):
            print(self.name,"walked",distance,"ft up.")
            self.position=int(self.position)+int(distance)
        else:
            print(self.name,"did not move.")

    def eat(self,food):
        self.food=food
        if(food=="Chocolate"):
            print(self.name,"ate some chocolate, it tasted great. +1HP")
            self.hp=int(self.hp)+1
        else:
            print(self.name,"ate some",food+", it didn't have any effect.")

class Dog(Creature):
    def __init__(self,name) -> None:
        self.name=name
        self.position=0
        self.hp=5

    def move(self,distance):
        self.distance=distance
        if(distance<0):
            print(self.name,"ran",abs(distance),"ft down.")
            self.position=int(self.position)+int(distance)
        elif(distance>0):
            print(self.name,"ran",distance,"ft up.")
            self.position=int(self.position)+int(distance)
        else:
            print(self.name,"sat still.")

    def eat(self,food):
        self.food=food
        if(food=="chocolate"):
            print(self.name,"ate some chocolate, dogs shouldn't eat chocolate. -1HP")
            self.hp=int(self.hp)-1
        else:
            print(self.name,"ate",food+", it tasted good.")

    def bark(self,volume):
        self.volume=abs(volume)
        if(volume>10):
            print(self.name,"barked really loud.")
        else:
            print(self.name,"barked.")

def main() -> None:
    jack=Human("Jack")
    buddy=Dog("Buddy")

    jack.move(15)
    buddy.move(-5)

    jack.eat("toast")
    buddy.eat("chocolate")
    buddy.bark(15)

main()
        


    


    
        
