class Horse:
    def __init__(self, Name, Height, Success):
        self.Name = Name #STRING
        self.MaxFenceHeight = Height #INTEGER
        self.PercentageSuccess = Success #INTEGER

    def GetPercentageSuccess(self):
        return self.PercentageSuccess
    def GetName(self):
        return self.Name
    def GetMaxFenceHeight(self):
        return self.MaxFenceHeight
    def SetPercentageSuccess(self, Success):
        self.PercentageSuccess = Success
    def SetName(self, Name):
        self.Name = Name
    def SetMaxFenceHeight(self, Height):
        self.MaxFenceHeight = Height
    def Success(self, Height, Risk):
        if Height > self.MaxFenceHeight:
            return 0.2 * self.PercentageSuccess
        match Risk:
            case 5: return 0.6 * self.PercentageSuccess
            case 4: return 0.7 * self.PercentageSuccess
            case 3: return 0.8 * self.PercentageSuccess
            case 2: return 0.9 * self.PercentageSuccess
            case 1: return self.PercentageSuccess

class Fence:
    def __init__(self, Height, Risk):
        self.Height = Height #INTEGER
        self.Risk = Risk #INTEGER
    def GetHeight(self):
        return self.Height
    def GetRisk(self):
        return self.Risk
    
    def SetHeight(self, Height):
        self.Height = Height
    def SetRisk(self, Risk):
        self.Risk = Risk

Horses = [Horse("Beauty", 150, 72), Horse("Jet", 160, 65)] #ARRAY OF Horse
print(Horses[0].GetName())
print(Horses[1].GetName())

Course = [Fence(0,0) for x in range(4)] #ARRAY OF Fence
for i in range(4):
    Height = 0 #INTEGER
    Risk = 0 #INTEGER
    while not 70 <= Height <= 180:
        Height = int(input(f"Enter the height from 70 - 180 for Fence {i+1}:"))
    while not 1 <= Risk <= 5:
        Risk = int(input(f"Enter the Risk from 1 - 5 for Fence {i+1}:"))
    Course[i] = Fence(Height, Risk)

for x in range(2):
    avg = 0 #INTEGER
    for y in range(4):
        print(f"The horse {Horses[x].GetName()} at Fence {y+1} has a {Horses[x].Success(Course[y].GetHeight(), Course[y].GetRisk())} %% chance of success.")
        avg += Horses[x].Success(Course[y].GetHeight(), Course[y].GetRisk())
    print(f"The horse {Horses[x].GetName()} has an average {avg/4} %% chance of success.")