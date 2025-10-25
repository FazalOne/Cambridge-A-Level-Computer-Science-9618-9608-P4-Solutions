def CreateDictionary():
    Dictionary = [["" for _ in range(2)] for _ in range(2000)] #2D ARRAY OF STRINGS
    return Dictionary

def hash(key):
    number = ord(key[0]) - 64 #INTEGER
    return number

def add(newkey, newvalue):
    index = hash(newkey) #INTEGER
    while dictionary[index][0] > "":
        index += 1
        if index >= 2000:
            index = 0 
    dictionary[index][0] = newkey
    dictionary[index][1] = newvalue

def delete(deletekey):
    index = hash(deletekey) #INTEGER
    while dictionary[index][0] != deletekey:
        index += 1
        if index >= 2000:
            index = 0
    dictionary[index][0] = ""
    dictionary[index][1] = ""

dictionary = CreateDictionary() #2D ARRAY OF STRINGS
add("File", "Datei")
add("Disk", "Platte")
add("Error", "Fehler")
add("Computer", "Rechner")
delete("Disk")
for entry in dictionary:
    if entry[0] != "":
        print(f"Key: {entry[0]}, Value: {entry[1]}")