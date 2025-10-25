class Card:
    def __init__(self, Num, CardColour):
        self.Number = Num #INTEGER
        self.Colour = CardColour #STRING
    def GetNumber(self):
        return self.Number
    def GetColour(self):
        return self.Colour

def chooseCard():
    global NumbersChosen
    flagContinue = True #BOOLEAN
    while flagContinue:
        CardSelected = int(input("Select a Card from 1 to 30: ")) #INTEGER
        if CardSelected < 1 or CardSelected > 30:
            print("Number must be between 1 and 30")
        elif NumbersChosen[CardSelected - 1]:
            print("Already taken")
        else:
            print("Valid")
            flagContinue = False
    NumbersChosen[CardSelected-1] = True
    return CardSelected-1

CardArray = [] #ARRAY OF CARDS
try:
    with open("CardValues.txt",'r') as File:
        for x in range(0,30):
            NumberRead = int(File.readline()) #INTEGER
            ColourRead = File.readline() #STRING
            CardArray += [Card(NumberRead, ColourRead)]
except FileNotFoundError:
    print("Could not find file")

NumbersChosen = [False for i in range(30)] #ARRAY OF BOOLEAN
Player1 = [] #ARRAY OF CARDS
for x in range(0, 4):
    ReturnNumber = chooseCard() #INTEGER
    Player1 += [CardArray[ReturnNumber]]
    print(Player1[x].GetNumber())
    print(Player1[x].GetColour())