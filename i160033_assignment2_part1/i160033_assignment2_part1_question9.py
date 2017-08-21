#question9
def listEquality(listA,listB):
    index=0
    if len(listA)!=len(listB):
        return False
    while index<len(listA):
        if listA[index]!=listB[index]:
            return False
        index+=1
    return True
listEquality(raw_input(),raw_input())
