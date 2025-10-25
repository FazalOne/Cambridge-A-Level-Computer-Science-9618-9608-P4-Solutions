Animal = ["" for x in range(20)] #ARRAY OF STRING
Colour = ["" for x in range(10)] #ARRAY OF STRING
AnimalTopPointer = 0 #INTEGER
ColourTopPointer = 0 #INTEGER

def PushAnimal(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer += 1
        return True

def PopAnimal():
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        AnimalTopPointer -= 1
        return Animal[AnimalTopPointer]
    
def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    else:
        Colour[ColourTopPointer] = DataToPush
        ColourTopPointer += 1
        return True

def PopColour():
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ColourTopPointer -= 1
        return Colour[ColourTopPointer]

def OutputItem():
    animal = PopAnimal() #STRING
    colour = PopColour() #STRING
    print(colour, animal)
    if colour == "":
        print("No colour")
        PushAnimal(animal)
    if animal == "":
        print("No animal")
        PushColour(colour)

def ReadData():
    try:
        with open("AnimalData.txt", "r") as File:
            data = File.readline().strip("\n") #STRING
            while data != "":
                PushAnimal(data)
                data = File.readline().strip("\n")
    except FileNotFoundError:
        print("Animal File not found, please open the correct folder or use the correct path")

    try:
        with open("ColourData.txt", "r") as File:
            data = File.readline().strip("\n")
            while data != "":
                PushColour(data)
                data = File.readline().strip("\n")
    except FileNotFoundError:
        print("Colour File not found, please open the correct folder or use the correct path")
ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()