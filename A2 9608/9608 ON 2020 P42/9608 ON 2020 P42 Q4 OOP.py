class FoodItem:
    def __init__(self,NewID):
        self.FoodID = NewID #STRING
        self.Name = "" #STRING
        self.Calories = 0 #INTEGER
    
    def GetFoodID(self):
        return self.FoodID
    def GetName(self):
        return self.Name
    def GetCalories(self):
        return self.Calories
    
    def SetFoodID(self,NewID):
        self.FoodID = NewID
    def SetName(self,NewName):
        self.Name=NewName
    def SetCalories(self,FoodCalories):
        if 0 < FoodCalories < 2000:
            self.Calories = FoodCalories
            return True
        else:
            return False