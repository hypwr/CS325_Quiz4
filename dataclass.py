from dataclasses import dataclass

@dataclass
class Food_Label:
    name:str
    servings:int
    serving_size:int #in grams by default
    #Amount Per Serving
    calories:int        
    total_fat:int       #in grams
    cholesterol:int     #in milligrams
    sodium:int          #in milligrams
    carbohydrates:int   #in grams, also includes sugar
    protein:int         #in grams

def main()->None:
    meal=[
        Food_Label("Cheez-it",18,30,150,8,0,270,18,3),
        Food_Label("Chicken Ramen",24,43,190,7,0,830,26,4),
        Food_Label("Coka-Cola",1,1,140,0,0,45,39,0)
    ]

    total_calories=0
    for x in meal:
        total_calories=total_calories+x.calories

    total_protein=0
    for x in meal:
        total_protein=total_protein+x.protein

    
    print("The total calories of one serving is: "+str(total_calories)+" Calories")
    print("The total grams of protein in one serving is: "+str(total_protein)+"g")

main()