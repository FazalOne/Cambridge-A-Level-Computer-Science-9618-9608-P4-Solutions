class Tree:
    def __init__(self, Name, Growth, MHeight,  MWidth, Green):
        self.TreeName = Name #STRING
        self.HeightGrowth = int(Growth) #INTEGER
        self.MaxHeight = int(MHeight) #INTEGER
        self.MaxWidth = int(MWidth) #INTEGER
        self.Evergreen = Green #STRING
    
    def GetTreeName(self):
        return self.TreeName
    def GetGrowth(self):
        return self.HeightGrowth
    def GetMaxHeight(self):
        return self.MaxHeight
    def GetMaxWidth(self):
        return self.MaxWidth
    def GetEvergreen(self):
        return self.Evergreen
    
def ReadData():
    DataArray = [] #ARRAY OF TREE
    #variant 1
    try:
        with open("Trees.txt") as file:
            data = file.read().split("\n") #ARRAY OF STRING
        for x in range(9):
            data[x] = data[x].split(",") # 2D ARRAY OF STRING
            DataArray.append(Tree(data[x][0],data[x][1],data[x][2],data[x][3],data[x][4]))
    except FileNotFoundError:
        print("Sorry, file not found. Check the filepath.")
    
    #variant 2
    # DataArray = []
    # try:
    #     with open("Trees.txt") as file:
    #         data = file.readline()
    #         while data != "":
    #             data = data.split(",")
    #             DataArray.append(Tree(data[0],data[1],data[2],data[3],data[4]))
    #             data = file.readline()
    # except FileNotFoundError:
    #     print("Sorry, file not found. Check the filepath.")
    return DataArray

def PrintTrees(Tree1):
    if Tree1.GetEvergreen() == "Yes":
        print('''{} has a maximum height {}, a maximum width {}, and grows {} cm a year. It does not lose its leaves.'''.format(Tree1.GetTreeName(), Tree1.GetMaxHeight(), Tree1.GetMaxWidth(), Tree1.GetGrowth()))
    else:
        print('''{} has a maximum height {}, a maximum width {}, and grows {} cm a year. It loses its leaves each year.'''.format(Tree1.GetTreeName(), Tree1.GetMaxHeight(), Tree1.GetMaxWidth(), Tree1.GetGrowth()))

def ChooseTree(DataArray):
    TreeSearch = [] #ARRAY OF TREE
    height = int(input("Enter the max height of tree: ")) #INTEGER
    width = int(input("Enter the max width of tree: ")) #INTEGER
    evergreen = ""
    while evergreen not in ["yes", "no"]:
        evergreen = input("Do you want an evergreen tree? Yes/No: ").lower() #STRING
    for TreeObj in DataArray:
        if TreeObj.GetMaxHeight() <= height and TreeObj.GetMaxWidth() <= width and TreeObj.GetEvergreen().lower() == evergreen:
            TreeSearch.append(TreeObj)
            PrintTrees(TreeObj)
    if len(TreeSearch) == 0:
        print("Sorry, no trees met your requirements.")
    else:
        found = False #BOOLEAN
        while not found:
            chosentree = input("Enter the name of the tree you have chosen: ").title() #STRING
            for x in TreeSearch:
                if x.GetTreeName() == chosentree:
                    found = True
                    chosentree = x
                    break
        buyheight = int(input("Enter the height of the tree at purchase time: ")) #INTEGER
        while buyheight > chosentree.GetMaxHeight():
            buyheight = int(input("Sorry, the height is greater than the tree's max height. Enter a valid height: "))
        time = (chosentree.GetMaxHeight() - buyheight) / chosentree.GetGrowth() #REAL
        print("{} will take {} years to grow to its max height".format(chosentree.GetTreeName(),time))

Trees = ReadData()
ChooseTree(Trees)