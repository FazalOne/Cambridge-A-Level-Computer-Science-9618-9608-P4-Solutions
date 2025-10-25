import pickle
class StockItem:
    def __init__(self) :
        self.ProductCode = "" #STRING
        self.Price = 0.0 #FLOAT
        self.NumberInStock = 0 #INTEGER

try:
    with open("StockFile", "rb") as file:
        StockData = pickle.load(file) #ARRAY OF StockItem
    for ThisStockItem in StockData:
        print(ThisStockItem.ProductCode)
        print(ThisStockItem.NumberInStock)
except FileNotFoundError:
    print("File does not exist")