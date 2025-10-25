class foodItem:
    def __init__(self, nameP, codeP, costP):
        self.name = nameP #STRING
        self.code = codeP #STRING
        self.cost = costP #REAL

    def getName(self):
        return self.name
    def getCode(self):
        return self.code
    def getCost(self):
        return self.cost

class vendingMachine:
    def __init__(self, item1, item2, item3, item4):
        self.items = [item1, item2, item3, item4] #ARRAY OF foodItem
        self.moneyIn = 0.0 #REAL

    def CheckValid(self, itemCode):
        for x in range(len(self.items)):
            if self.items[x].getCode() == itemCode:
                if self.items[x].getCost() <= self.moneyIn:
                    return x
                return -2
        return -1
    def insertMoney(self, money):
        self.moneyIn += money
    def getItemName(self, index):
        return self.items[index].getName()
    
chocolate = foodItem("Chocolate", 1001, 10.0) #foodItem
sweets = foodItem("Sweets", 1002, 5.0) #foodItem
sandwich = foodItem("Sandwich", 1003, 15.0) #foodItem
apple = foodItem("Apple", 1004, 7.0) #foodItem
vendor = vendingMachine(chocolate, sweets, sandwich, apple) #vendingMachine