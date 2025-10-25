class Booking:
    def __init__(self):
        self.BookingID = 0 #INTEGER
        self.CustomerID = 0 #INTEGER
        self.ItemID = 0 #INTEGER
        self.Quantity = 0  #INTEGER

def Hash(BookingID):
    Value = BookingID % 100000 + 3 #INTEGER
    return Value

def StoreBooking(BookingRecord):
    RecordLocation = Hash(BookingRecord.BookingID) #INTEGER
    Filename = "TheBookings.dat" #STRING
    file = open(Filename, "rb+")
    file.seek(RecordLocation)
    RecordData = file.read() #STRING
    if RecordData == "":
        file.write(BookingRecord)
        file.close()
        return True
    else:
        file.close()
        return False