class Cards:
    def __init__(self, Num, theShape):
        if 0 <= Num <= 9 and theShape in ["square", "triangle", "circle"]:
            self.Number = Num #INTEGER
            self.Shape = theShape #STRING
        else:
            print("Error")
    
    def GetNumber(self):
        return self.Number
    def GetShape(self):
        return self.Shape
    
OneS = Cards(1, "square") #Cards

def Compare(Card1, Card2):
    if Card1.GetNumber() == Card2.GetNumber() and Card1.GetShape() == Card2.GetShape():
        print("SNAP")
        return -1
    elif Card2.GetNumber() > Card1.GetNumber():
        return Card2.GetNumber()
    else:
        return Card1.GetNumber()