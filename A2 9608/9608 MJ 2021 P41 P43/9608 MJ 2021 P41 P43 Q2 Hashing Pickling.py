import pickle
class Customer:
    def __init__(self):
        self.customerID = 0 #INTEGER
        self.firstName = "" #STRING
        self.lastName = "" #STRING
        self.telephoneNumber = "" #STRING

def getRecordLocation(CustID):
    return (CustID.customerID % 1000) + 2

def getCustomer(customerID):
    filename = "customerRecords.dat" #STRING
    customerFile = open(filename,'rb')
    customerFile.seek(getRecordLocation(customerID))
    Record = pickle.load(customerFile)
    customerFile.close()
    return Record