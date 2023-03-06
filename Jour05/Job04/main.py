def maxOfList(list):
    if len(list) == 1:
        return list[0]
    else:
        return max(list[0], maxOfList(list[1:]))
    
list = [1,13,2,59,3,5,7,55]
print(maxOfList(list))
