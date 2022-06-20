def swapPosition(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

list = [19, 56, 23,45]
print(len(list))
pos1, pos2 = 1, 4

print(swapPosition(list, pos1-1, pos2-1))