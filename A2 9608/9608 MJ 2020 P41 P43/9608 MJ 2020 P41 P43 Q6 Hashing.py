class CustomerRecord:
    def __init__(self, UserID, PINNumber):
        self.UserID = UserID #STRING
        self.PINNumber = PINNumber #INTEGER

def InitialiseHashTable():
    CustomerDetails = [CustomerRecord("", "") for _ in range(6000)] #ARRAY OF CustomerRecord
    return CustomerDetails

def InsertRecord(NewRecord):
    Count = 0
    Index = Hash(NewRecord.UserID)  # Assuming UserID is a key in the new_record dictionary
    while CustomerDetails[Index].UserID != "" and Count <= 5999:
        Index += 1
        Count += 1
        if Index > 5999:
            Index = 0
    if Count > 5999:
        return -1
    else:
        CustomerDetails[Index] = NewRecord
        return Index

CustomerDetails = InitialiseHashTable() 