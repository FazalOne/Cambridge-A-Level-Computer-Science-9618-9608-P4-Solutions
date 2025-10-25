StoredData = [-1 for x in range(10000)] #ARRAY OF INTEGERS

def AddItem(DataToAdd):
    Location = (DataToAdd % 1000) + 6 #INTEGER
    if StoredData[Location] != -1:
        Found = False #BOOLEAN
        Counter = 0 #INTEGER
        while Found == False and Counter < 9999:
            Location += 1
            if Location > 9999:
                Location = 0
            if StoredData[Location] == -1:
                Found = True
                Counter += 1
            if Found:
                StoredData[Location] = DataToAdd
            return Found
    else:
        StoredData[Location] = DataToAdd
        return True