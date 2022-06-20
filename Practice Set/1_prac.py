# swapping first element with last element of the list.
# we are using len function

def swapFunc(newList):
    size = len(newList)

    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp

    return newList  


newList = [12, 45, 7, 16, 25]
print(swapFunc(newList))