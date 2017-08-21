#question 12
def permutation():
    listA=[27,15,15,11,27,9,13,45,22,78,13,9]
    listB=[27,15,9]
    index=0
    while index<len(listB):
        if listB[index] not in listA:
            return False
        
        index+=1
    return True
permutation()
