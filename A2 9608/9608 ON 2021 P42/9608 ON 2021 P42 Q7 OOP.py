class Box:
    def __init__(self, SizeString, LockNumber):
        self.Size = SizeString #STRING
        self.Lock = LockNumber #STRING
        self.Strength = 100 #INTEGER
        self.Contents = [0 for x in range(10)] #ARRAY OF INTEGERS

    def Unlock(self, Key):
        if self.Lock == Key:
            return True
        else:
            self.Strength -= 1
            return self.Strength <= 0 
            
    def LoadGame():
        Filename = "progress.txt" #STRING
        try:
            with open(Filename, "r") as F:
                GameData = F.read()
        except FileNotFoundError:
            print("File not found")
            
    def GetContents(self):
        return self.Contents
    
    def SetSize(self, NewSize):
        self.Size = NewSize
    def SetContents(self, NewContent):
        self.Contents = NewContent
    def SetLock(self, NewLock):
        self.Lock = NewLock
    def SetStrength(self, NewStrength):
        self.Strength = NewStrength