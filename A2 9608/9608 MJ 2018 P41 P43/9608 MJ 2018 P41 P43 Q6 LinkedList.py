class node:
    def __init__(self, Player, Pointer):
        self.Player = Player #STRING
        self.Pointer = Pointer #INTEGER

def outputNodes(Scorers, currentPointer):
    while(currentPointer != -1):
        print(str(Scorers[currentPointer].Player))
        currentPointer = Scorers[currentPointer].Pointer

def SearchList(Find, Position):
    if Scorers[Position].Player == Find:
        return Position
    else:
        if Scorers[Position].Player != -1:
            return SearchList(Find, Scorers[Position].Pointer)
        else:
            return 99

Scorers = [node("Alvaro",1),node("Antoine",3),node("Dimitri",7),node("Cristiano",2),node("Gareth",5),node("Graziano",6),node("Olivier",8),node("Erik",4),node("Yaya",9),node("Zoto",-1)] #ARRAY OF nodes
startPointer = 0 #INTEGER
outputNodes(Scorers, startPointer)
print(SearchList("Gareth",startPointer))