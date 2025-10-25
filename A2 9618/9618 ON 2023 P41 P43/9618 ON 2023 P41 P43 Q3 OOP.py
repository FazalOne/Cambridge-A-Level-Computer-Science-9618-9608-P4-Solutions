from unittest import case


class Character: 
	def __init__(self, XPositionP, YPositionP, NameP):
		self.XPosition = XPositionP #INTEGER
		self.YPosition = YPositionP #INTEGER
		self.Name = NameP #STRING
	
	def GetXPosition(self): 
		return self.XPosition
	def GetYPosition(self): 
		return self.YPosition
	def SetXPosition(self, Value):
		self.XPosition += Value
		if self.XPosition > 10000:
			self.XPosition = 10000 
		elif self.XPosition < 0:
			self.XPosition = 0
	def SetYPosition(self, Value): 
		self.YPosition += Value 
		if self.YPosition > 10000:
			self.YPosition = 10000 
		elif self.YPosition < 0:
			self.YPosition = 0
	
	def Move(self, Direction): 
		match Direction:
			case "up": self.SetYPosition(10) 
			case "down": self.SetYPosition(-10) 
			case "right": self.SetXPosition(10) 
			case "left": self.SetXPosition(-10)

class BikeCharacter(Character):
	def __init__(self, XPositionP, YPositionP, NameP): 
		super().__init__(XPositionP, YPositionP, NameP)
	def Move(self, Direction): 
		match Direction:
			case "up": super().SetYPosition(20) 
			case "down": super().SetYPosition(-20) 
			case "right": super().SetXPosition(20) 
			case "left": super().SetXPosition(-20)

Jack = Character(50, 50, "Jack") #Character
Karla = BikeCharacter(100, 50, "Karla") #BikeCharacter

CharacterToMove = input("Would you like to move Jack or Karla?: ").lower() #STRING
while CharacterToMove not in ["jack","karla"]:
	CharacterToMove = input("Invalid try again: ")
Direction = input("Which direction? up, down, left or right?: ").lower() #STRING
while Direction not in ["up","down","left","right"]:
	Direction = input("Invalid try again: ") 
if CharacterToMove == "jack":
	Jack.Move(Direction)
	print("Jack's new position is X =", Jack.GetXPosition(), "Y =", Jack.GetYPosition())
else:
	Karla.Move(Direction)
	print("Karla's new position is X =", Karla.GetXPosition(), "Y =", Karla.GetYPosition())