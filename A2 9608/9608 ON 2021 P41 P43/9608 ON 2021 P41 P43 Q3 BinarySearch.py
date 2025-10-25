def BinarySearch(ThisArray, LowerBound, UpperBound, SearchValue):
    flag = -2 #INTEGER
    while flag != -1:
        mid = LowerBound + ((UpperBound - LowerBound) // 2) #INTEGER
        if UpperBound < LowerBound:
            return -1
        else:
            if ThisArray[mid] > SearchValue:
                UpperBound = mid - 1
            elif ThisArray[mid] < SearchValue:
                LowerBound = mid + 1
            else:
                return mid