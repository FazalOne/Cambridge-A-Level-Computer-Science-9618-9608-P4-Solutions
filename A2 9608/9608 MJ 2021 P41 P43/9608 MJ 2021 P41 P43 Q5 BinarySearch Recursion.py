def binarySearch(upper, lower, searchValue):
    flag = -2 #INTEGER
    mid = 0 #INTEGER
    while flag != -1:
        mid = lower + ((upper - lower) // 2)
        if upper < lower:
            return -1
        else:
            if dataArray[mid] < searchValue:
                lower = mid + 1
            elif dataArray[mid] > searchValue:
                upper = mid - 1
            else:
                return mid

def recursiveBinarySearch(lowerbound, upperbound, searchValue):
    mid = lowerbound + ((upperbound - lowerbound) // 2) #INTEGER
    if upperbound < lowerbound:
        return -1
    else:
        if dataArray[mid] < searchValue:
            return recursiveBinarySearch(mid + 1, upperbound, searchValue)
        elif dataArray[mid] > searchValue:
            return recursiveBinarySearch(lowerbound, mid - 1, searchValue)
        else:
            return mid
