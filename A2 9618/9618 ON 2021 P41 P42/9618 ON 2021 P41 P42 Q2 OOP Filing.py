class Picture:
    def __init__(self, Desc, W, H, Color):
        self.Description = Desc #STRING
        self.Width = W #INTEGER
        self.Height = H #INTEGER
        self.FrameColour = Color #STRING

    def GetDescription(self):
        return self.Description
    def GetHeight(self):
        return self.Height
    def GetWidth(self):
        return self.Width
    def GetColor(self):
        return self.FrameColour
    def SetDescription(self, newDesc):
        self.Description = newDesc

def ReadData():
    global DataArray
    try:
        with open("Pictures.txt", "r") as File:
            count = 0 #INTEGER
            Data = File.readline().strip("\n") #STRING
            while Data != "":
                Desc = Data #STRING
                Width = int(File.readline().strip("\n")) #INTEGER
                Height = int(File.readline().strip("\n")) #INTEGER
                Frame = File.readline().strip("\n") #STRING
                Data = File.readline().strip("\n")
                DataArray[count] = Picture(Desc, Width, Height, Frame)
                count += 1
        return count
    except FileNotFoundError:
        print("File not found. Please check your file path.")
        return 0

DataArray = [Picture("",0,0,"") for x in range(100)] #ARRAY OF Pictures
PictureCount = ReadData() #INTEGER
UserFrame = input("Enter frame color: ").lower() #STRING
UserHeight = int(input("Enter height: ")) #INTEGER
UserWidth = int(input("Enter width: ")) #INTEGER
for x in range(PictureCount):
    if DataArray[x].GetColor().lower() == UserFrame and DataArray[x].GetHeight() <= UserHeight and DataArray[x].GetWidth() <= UserWidth:
        print("Description: ", DataArray[x].GetDescription())
        print("Width: ", DataArray[x].GetWidth())
        print("Height: ", DataArray[x].GetHeight())