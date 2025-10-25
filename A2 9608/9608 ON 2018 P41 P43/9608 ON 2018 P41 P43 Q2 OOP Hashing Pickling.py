import pickle
class Book:
    def __init__(self,Title,Author,ISBN,Fiction,LastRead):
        self.Title = Title #STRING
        self.Author = Author #STRING
        self.ISBN = ISBN #INTEGER
        self.Fiction = Fiction #STRING
        self.LastRead = LastRead #STRING
    def Print(self):
        print("Book Title: {} , Book Author: {} , Book ISBN: {} , Fiction: {} , Last Read: {}".format(self.Title,self.Author, self.ISBN, self.Fiction, self.LastRead))
    
def Hash(ISBN):
    return (int(ISBN) % 2000) + 1

def AddBook():
    prompt = "y" #STRING
    global YesResponses, NoResponses, BookList
    while prompt in YesResponses:
        print("Please enter the Book details below.") 
        BookTitle = input("Please enter title of Book: ") 
        BookAuthor = input(f"Please enter the name of Author of {BookTitle}: ") 
        BookISBN = input("Please enter the ISBN of the book: ")

        while len(BookISBN) != 13:
            print("Invalid ISBN. Please enter the 13 digit ISBN number.")
            BookISBN = input("Please enter the ISBN of the book you wish to search: ")

        BookFiction = input("Is the genre Fiction or not? (Y/N): ")
        while BookFiction not in YesResponses and BookFiction not in NoResponses:
            print("Invalid entry, please try again")
            BookFiction = input("Is the book genre Fiction or not? (Y/N): ")
        BookFiction = BookFiction in YesResponses

        LastReadDate = input(f"Please enter the date when you last read {BookTitle}: ")
        BookRecord = Book(BookTitle,BookAuthor,BookISBN,BookFiction,LastReadDate) #Book
        BookList[Hash(BookISBN)] = BookRecord
        prompt = input("Do you wish to add another book to your list?: (Y/N)")
    with open("MyBook.DAT","wb+") as BookFile:
        pickle.dump(BookList,BookFile) 

def FindBook():
    with open("MyBook.DAT","rb+") as BookFile:
        BookSavedList = pickle.load(BookFile) 
    prompt = "y" #STRING
    global YesResponses, NoResponses, BookList
    while prompt in YesResponses:
        BookISBN = input("Please enter the ISBN of the book you wish to search: ")
        while len(BookISBN) != 13:
            print("Invalid ISBN. Please enter the 13 digit ISBN number.")
            BookISBN = input("Please enter the ISBN of the book you wish to search: ")
        Index = Hash(BookISBN)
        BookSavedList[Index].Print()
        prompt = input("Do you wish to search another ISBN? (Y/N): ")

BookList = [0 for x in range(2001)] #ARRAY OF Books
YesResponses = ["yes","Yes","Y","y"] #ARRAY OF STRINGS
NoResponses = ["no","No","N","n"] #ARRAY OF STRINGS
AddBook()
FindBook()