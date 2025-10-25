class StockItem:
    def __init__(self, title, acqdate):
        self.Title = title #STRING
        self.AcqDate = acqdate #STRING
        self.OnLoan = False #BOOLEAN
    
    def ShowTitle(self):
        return self.Title
    def ShowAcqDate(self):
        return self.AcqDate
    def CheckLoan(self):
        return self.OnLoan
    def SetLoan(self):
        self.OnLoan = not self.OnLoan
    def OutputDetails(self):
        return "Stock Title: {}, Acquisition Date: {}, On Loan: {}".format(self.Title, self.AcqDate, self.OnLoan)

class Book(StockItem):
    def __init__(self, title, acqdate, author, isbn):
        super().__init__(title, acqdate)
        self.Author = author #STRING
        self.ISBN = isbn #STRING

    def ShowAuthor(self):
        return self.Author
    def ShowISBN(self):
        return self.ISBN
    def OutputDetails(self):
        return "{}, Author: {}, ISBN: {}".format(super().OutputDetails(), self.Author, self.ISBN)
    
class CD(StockItem):
    def __init__(self, title, acqdate, artist, playtime):
        super().__init__(title, acqdate)
        self.Artist = artist #STRING
        self.Playtime = playtime #INTEGER

    def ShowArtist(self):
        return self.Artist
    def ShowPlaytime(self):
        return self.Playtime
    def OutputDetails(self):
        return "{}, Artist: {}, Playtime: {}".format(super().OutputDetails(), self.Artist, self.Playtime)
    
NewBook = Book("Computers", "12/11/2002", "A.Nyone", "099111") #BOOK
NewCD = CD("Greatest Hits", "01/01/2000", "Some Artist", 60) #CD
print(NewBook.OutputDetails())
print(NewCD.OutputDetails())