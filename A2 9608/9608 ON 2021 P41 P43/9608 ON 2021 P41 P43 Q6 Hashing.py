class CustomerData:
    def __init__(self):
        self.CustomerID = "" #STRING
        self.FirstName = "" #STRING
        self.SecondName = "" #STRING

def StoreRecord(NewData):
    HashValue = CustomerHash(NewData.CustomerID) #INTEGER
    Filename = "CustomerRecords.dat" #STRING
    with open(Filename, 'rb+') as file:
        file.seek(HashValue)
        file.write(NewData)