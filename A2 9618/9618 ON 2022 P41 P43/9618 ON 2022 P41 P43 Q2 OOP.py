class Card:
    def __init__(self, Number, Colour):
        self.Number = Number #INTEGER
        self.Colour = Colour #STRING

    def GetNumber(self):
        return self.Number
    def GetColour(self):
        return self.Colour
    
class Hand:
    def __init__(self, Card1, Card2, Card3, Card4,Card5):
        self.Cards = [Card1, Card2, Card3, Card4, Card5] #ARRAY OF Cards
        self.FirstCard = 0 #INTEGER
        self.NumberCards = 5 #INTEGER

    def GetCard(self, Position):
        return self.Cards[Position]

def CalculateValue(Player):
    Score = 0
    for Count in range(0, 5):
        CardTaken = Player.GetCard(Count)
        Score += CardTaken.GetNumber()
        Colour = CardTaken.GetColour()
        match Colour:
            case "red" : Score += 5
            case "blue" : Score += 10
            case "yellow" : Score += 15
    return Score

OneRed = Card(1, "red") #Card
TwoRed = Card(2, "red") #Card
ThreeRed = Card(3, "red") #Card
FourRed = Card(4, "red") #Card
FiveRed = Card(5, "red") #Card
OneBlue = Card(1, "blue") #Card
TwoBlue = Card(2, "blue") #Card
ThreeBlue = Card(3, "blue") #Card
FourBlue = Card(4, "blue") #Card
FiveBlue = Card(5, "blue") #Card
OneYellow = Card(1, "yellow") #Card
TwoYellow = Card(2, "yellow") #Card
ThreeYellow = Card(3, "yellow") #Card
FourYellow = Card(4, "yellow") #Card
FiveYellow = Card(5, "yellow") #Card
Player1 = Hand(OneRed, TwoRed, ThreeRed, FourRed, OneYellow) #Hand
Player2 = Hand(TwoYellow, ThreeYellow, FourYellow, FiveYellow, OneBlue) #Hand
PScore1 = CalculateValue(Player1)
PScore2 = CalculateValue(Player2)
if PScore1 > PScore2:
    print("Player 1 wins")
elif PScore1 < PScore2:
    print("Player 2 wins")
else:
    print("It's a draw")