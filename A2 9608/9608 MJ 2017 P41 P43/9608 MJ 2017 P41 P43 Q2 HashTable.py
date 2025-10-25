import random

class CustomerRecord():
    def __init__(self, CustID, Details):
        self.CustomerID = CustID
        self.Data = Details

def CreateHashTable():
    return [CustomerRecord(0,"") for x in range(200)] #ARRAY OF CustomerRecords

def Hash(CustID):
    return CustID % 200

def InsertRecord(NewCustomer):
    TableFull = False #BOOLEAN
    Index = Hash(NewCustomer.CustomerID) #INTEGER
    print("Hash is ",Index)
    Pointer = Index #INTEGER
    while Customers[Pointer].CustomerID > 0:
        if Pointer > 199:
            Pointer = 0
        if Pointer == Index:
            TableFull = True
        Pointer += 1
    if not TableFull:
        Customers[Pointer] = NewCustomer
    else:
        print("Error")

def SearchHashTable(SearchID):
    Index = Hash(SearchID) #INTEGER
    while Customers[Index].CustomerID != SearchID and Customers[Index].CustomerID > 0:
        if Index > 199:
            Index = 0
        Index += 1
    if Customers[Index].CustomerID == SearchID:
        return Index
    else:
        return -1

Customers = CreateHashTable() #ARRAY OF CustomerRecords
NewCustomer = CustomerRecord(random.randint(10000,99999),"Name: Jason, Age: 34")
InsertRecord(NewCustomer)
CustIndex = SearchHashTable(NewCustomer.CustomerID) #INTEGER
print(Customers[CustIndex].Data)