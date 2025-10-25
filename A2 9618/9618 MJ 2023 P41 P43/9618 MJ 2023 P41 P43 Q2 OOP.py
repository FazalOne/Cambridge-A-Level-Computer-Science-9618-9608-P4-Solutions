class Vehicle:
    def __init__(self, ID, MaxSpeed, IncreaseAmount):
        self.ID = ID #STRING
        self.MaxSpeed = MaxSpeed #INTEGER
        self.IncreaseAmount = IncreaseAmount #INTEGER
        self.CurrentSpeed = 0 #INTEGER
        self.HorizontalPosition = 0 #INTEGER
    def GetCurrentSpeed(self):
        return self.CurrentSpeed
    def GetIncreaseAmount(self):
        return self.IncreaseAmount
    def GetMaxSpeed(self):
        return self.MaxSpeed
    def GetHorizontalPosition(self):
        return self.HorizontalPosition
    def SetCurrentSpeed(self, newSpeed):
        self.CurrentSpeed = newSpeed
    def SetHorizontalPosition(self, newHPos):
        self.HorizontalPosition = newHPos
    def IncreaseSpeed(self):
        self.CurrentSpeed += self.IncreaseAmount
        if self.CurrentSpeed > self.MaxSpeed:
            self.CurrentSpeed = self.MaxSpeed
        self.HorizontalPosition += self.CurrentSpeed
    def Details(self):
        return "Horizontal Position: {}, Current Speed: {}".format(self.HorizontalPosition, self.CurrentSpeed)

class Helicopter(Vehicle):
    def __init__(self, ID, MaxSpeed, IncreaseAmount, VChange, MaxHeight):
        super().__init__(ID, MaxSpeed, IncreaseAmount)
        self.VerticalPosition = 0 #INTEGER
        self.VerticalChange = VChange #INTEGER
        self.MaxHeight = MaxHeight #INTEGER
    def IncreaseSpeed(self):
        super().IncreaseSpeed()
        self.VerticalPosition += self.VerticalChange
        if self.VerticalPosition > self.MaxHeight:
            self.VerticalPosition = self.MaxHeight
    def Details(self):
        return "{} , Vertical Position: {}".format(super().Details(), self.VerticalPosition)
    
def Output(vehicle):
    print(vehicle.Details())

Car = Vehicle("Tiger", 100, 20) #Vehicle
Chopper = Helicopter("Lion", 350, 40, 3, 100) #Helicopter
Car.IncreaseSpeed()
Car.IncreaseSpeed()
Output(Car)
Chopper.IncreaseSpeed()
Chopper.IncreaseSpeed()
Output(Chopper)