def Count(Number):
    if Number % 2 != 0:
        Number -= 1
    print(Number)
    if Number > 0:
        Count(Number - 1)

def MealsCount(MealOption1, MealOption2):
    MealOption = int(input("Enter meal option: ")) #INTEGER
    if MealOption == 1:
        MealOption1 += 1
        MealsCount(MealOption1, MealOption2)
    elif MealOption == 2:
        MealOption2 += 1
        MealsCount(MealOption1, MealOption2)
    else:
        print(MealOption1, " ", MealOption2)
   
Count(6)
MealsCount(0,0)