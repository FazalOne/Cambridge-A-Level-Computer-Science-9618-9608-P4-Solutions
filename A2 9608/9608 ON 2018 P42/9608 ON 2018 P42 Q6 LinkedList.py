class ListElement:
    def __init__(self, CountryP,PointerP):
        self.Country = CountryP #STRING
        self.Pointer = PointerP #INTEGER

def outputListElements(CountryList, currentPointer):
    while(currentPointer != -1):
        print(str(CountryList[currentPointer].Country))
        currentPointer = CountryList[currentPointer].Pointer

def DeleteNode(NodeValue, ThisPointer, PreviousPointer):
    global CountryList, ListHead, LastListElement
    if CountryList[ThisPointer].Country == NodeValue:
        CountryList[ThisPointer].Country = ""
        if ListHead == ThisPointer:
            ListHead = CountryList[ThisPointer].Pointer
        else:
            CountryList[PreviousPointer].Pointer = CountryList[ThisPointer].Pointer
        CountryList[LastListElement].Pointer = ThisPointer
        LastListElement = ThisPointer
        CountryList[ThisPointer].Pointer = -1
    else:
        if CountryList[ThisPointer].Pointer != -1:
            DeleteNode(NodeValue, CountryList[ThisPointer].Pointer, ThisPointer)
        else:
            print("DOES NOT EXIST")

CountryList = [ListElement("Wales",1),
               ListElement("Scotland",3),
               ListElement("",-1),
               ListElement("England",4),
               ListElement("Brazil",5),
               ListElement("Canada",6),
               ListElement("Mexico",7),
               ListElement("Peru",8),
               ListElement("China",9),
               ListElement("",10),
               ListElement("",11),
               ListElement("",12),
               ListElement("",13),
               ListElement("",14),
               ListElement("",2)] #ARRAY OF ListElements
ListHead = 0 #INTEGER
LastListElement = 2 #INTEGER
outputListElements(CountryList, ListHead)
DeleteNode("Peru",0,0)
outputListElements(CountryList, ListHead)